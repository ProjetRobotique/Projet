Méthodes potentiellement utiles :
	
	- after(delai_ms, fonc=None, *args)
		- Demande à Tkinter d’appeller la fonction de rappel fonc avec les arguments args après l’écoulement du délai delai_ms donné en millisecondes. 
		Votre fonction de rappel ne peut pas être appelée avant ce délai (même si son appel effectif peut le dépasser) et elle ne sera appelée qu’une fois.
		Elle retourne un entier qui sert d’identifiant et qui peut être passé à la méthode after_cancel pour annuler la demande d’appel de fonc.
		Si vous ne donnez aucune fonction de rappel, cette fonction arrête l’exécution du programme pendant la durée du délai indiqué (comme la fonction standard sleep du module time).
		
	- bell()
		- Produit un son, généralement un bip
	
	- destroy()
		- L’appel w.destroy() sur un widget w détruit w ainsi que tous ses enfants.
	
	- focus_force()
		- Force le focus sur le widget appelant. Ce n’est pas très poli. Il vaut mieux attendre que le gestionnaire de fenêtre donne lui-même le focus. Voir aussi la méthode grab_set_global() ci-dessous.
	
	- lift(aboveThis=None)
		- Si l’argument est None, la fenêtre qui contient le widget appelant est déplacée tout en haut de la pile des fenêtres.
		  Pour déplacer la fenêtre juste au-dessus d’une fenêtre principale f, la fournir en argument.
	
	- quit()
		- Cette méthode fait sortir de la boucle des événéments (mainloop). Voir la méthode mainloop() ci-dessous pour plus d’informations sur la boucle des événements.

	- selection_get()
		- Si le widget appelant possède une sélection, cette méthode retourne le texte sélectionné. Sinon, une erreur du type TclError est levée.
	
	- update()
		- Cette méthode force le rafraîchissement de l’affichage. Vous ne devriez l’utiliser que si vous savez ce que vous faites puisqu’elle peut conduire 
		  à un comportement imprévisible ou à une boucle infinie. Dans tous les cas, elle ne devrait jamais être appelée à partir d’un gestionnaire d’événement 
		  ou d’une fonction appelée par un tel gestionnaire.
		  
	- update_idletasks()
		- certaines tâches dans la mise à jour de l’affichage, comme l’agrandissement/réduction d’un widget, sont dites dormantes ou en sommeil (idle) parce qu’elles 
		  sont normalement reportées jusqu’au moment où l’application a terminé de s’occuper des événements et est revenue dans la boucle principale pour attendre les prochains.
		  Si vous souhaitez forcer le rafraîchissement de l’affichage avant que l’application soit de nouveau en sommeil, appelez cette méthode sur un widget arbitraire.
	
	
	
Documentation :
	
	- http://tkinter.fdex.eu/doc/
	
		
