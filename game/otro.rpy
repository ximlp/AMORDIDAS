init python:

    # Diccionario de tamaños por fuente y escala
    size_dict = {
        "MarcellusRegular.ttf": {
            "regular": 32,
            "large": 38,
            "line_spacing": 0,
        },
        "OpenDyslexic.otf": {
            "regular": 30,
            "large": 36,
            "line_spacing": -5,
        },
    }

    # Cambia la fuente y ajusta tamaño y espaciado
    def changeFont(newFont):
        return (
            SetField(persistent, "pref_text_font", newFont),
            SetField(persistent, "pref_text_size", size_dict[newFont][persistent.pref_text_scale]),
            SetField(persistent, "pref_text_spacing", size_dict[newFont]["line_spacing"]),
            SelectedIf(persistent.pref_text_font == newFont)
        )

    # Cambia la escala del texto (tamaño)
    def changeScale(newScale):
        return (
            SetField(persistent, "pref_text_scale", newScale),
            SetField(persistent, "pref_text_size", size_dict[persistent.pref_text_font][newScale])
        )

    # Cambia el color del texto
    def changeColor(newColor):
        return SetField(persistent, "pref_text_color", newColor)

    # Alterna cualquier campo persistent True/False
    def persistentToggle(persistentfield):
        return ToggleField(persistent, persistentfield, true_value=True, false_value=False)

#Valores por defecto (se colocan fuera de init)
default persistent.pref_text_font = "fonts/MarcellusRegular.ttf"
default persistent.pref_text_scale = "regular"
default persistent.pref_text_size = 32
default persistent.pref_text_spacing = 0
default persistent.pref_text_color = "#ffffff"
default persistent.audio_cues = True
default persistent.screenshake = True