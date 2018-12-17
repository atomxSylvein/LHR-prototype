from odoo import http
from odoo.http import request

class Main(http.Controller):

	@http.route('/portail-lhr', auth='public', website=True)
	def portail_lhr(self):
		return request.render('lhr_portal.accueil', {} )

	@http.route('/portail-lhr/formulaire-contact', auth='public', website=True)
	def formulaire_devis(self):
		return request.render('lhr_portal.create_operation', {} )

	@http.route('/portail-lhr/lhr-created', type='http', auth='public', website=True)
	def create_devis(self, **post):

		#Create contact first
		contact = request.env['res.partner'].sudo().create({
			'name': ' '.join([post.get('prenom'), post.get('nom')]),
			'phone': str(post.get('telephone')),
			'email': post.get('email'),
			'x_gender': 'man' if str(post.get('sexe')) == 'Homme' else 'woman',
			'x_years_old': int(post.get('age')),
			'x_greffe': True if post.get('greffe') else False,
		})

		#then create new operation with status
		operation_environment = request.env['graft.operation']
		operation = operation_environment.sudo().create({
			'm_client': int(contact.id),
			'm_message': post.get('message'),
		})
		return http.request.redirect('/portail-lhr')