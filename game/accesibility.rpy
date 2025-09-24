screen accesibilidad():

    tag menu
    use game_menu("Accesibilidad")

    vbox:
        style_prefix "pref"
        xsize 1800
        xalign 0.5
        ypos 250
        ysize 800

        fixed:

            viewport:
                #scrollbars "vertical"
                if main_menu:
                    xoffset 0
                    xsize 1700
                else:
                    xoffset 200
                    xsize 1920
                mousewheel True

                hbox:
                
                    vbox:

                        label _("Fuente")

                        null height 10

                        textbutton _(" Por defecto"):
                            action Preference("font transform", "dejavusans")
                            style_suffix "radio_button"

                        textbutton _(" Serif"):
                            action Preference("font transform", "javusans")
                            style_suffix "radio_button"

                        textbutton _(" Opendyslexic"):
                            action Preference("font transform", "opendyslexic")
                            style_suffix "radio_button"

                        null height 40
                        
                        label _(" High Contrast Text")
                        
                        textbutton _(" Activar"):
                            action Preference("high contrast text", "enable")
                            style_suffix "radio_button"

                        textbutton _(" Desactivar"):
                            action Preference("high contrast text", "disable")
                            style_suffix "radio_button"
                    
                    vbox:
                        xoffset -50

                        label _("Tamaño de texto")

                        null height 10

                        bar value Preference("font size")

                        textbutton _("Reset"):
                            text_size 25
                            alt "reset font size"
                            action Preference("font size", 1.0)

                        null height 40

                        label _("Interlineado")

                        null height 10

                        bar value Preference("font line spacing")
                        
                        textbutton _("Reset"):
                            text_size 25
                            alt "reset font line spacing"
                            action Preference("font line spacing", 1.0)
                        null height 40
                        text "Sonido a texto" color "#000000"
                        vbox:
                            spacing 0
                            textbutton " Descripción de efectos de sonido" action ToggleField(persistent, "audio_cues", True, False):
                                style_suffix "radio_button"
                        
                        
                    null width 50
                    vbox:

                        label _("Voice Volume")

                        null height 10

                        bar value Preference("voice volume")

                        null height 40

                        label _("Self-Voicing Volume Drop")

                        null height 10

                        bar value Preference("self voicing volume drop")

                        null height 40

                        label _(" Texto a voz")

                        if renpy.variant("touch"):
                            text _("Self-voicing support is limited when using a touch screen.")
                        null height 10

                        textbutton _(" Apagado"):
                            action Preference("self voicing", "disable")
                            style_suffix "radio_button"

                        textbutton _(" Texto a voz"):
                            action Preference("self voicing", "enable")
                            style_suffix "radio_button"
                        
                        
                    