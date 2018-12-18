from odoo import http
from odoo.http import request

from odoo.addons.website.controllers.main import Website

class Main(Website):

	#homepage
	@http.route('/', type='http', auth='public', website=True)
	def index(self, **kw):
		return request.render('lhr_portal.accueil', {} )

	@http.route('/formulaire-contact', auth='public', website=True)
	def formulaire_devis(self):
		return request.render('lhr_portal.create_operation', {} )

	@http.route('/lhr-created', type='http', auth='public', website=True)
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
		return http.request.redirect('/')