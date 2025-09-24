##### AMORDIDAS // AVOCADO STUDIO // EMILIO VELAZQUEZ, FRANCISCO GUZMAN // XIMENA LEON
#12
##### Declaración de personajes
define he = Character("Helena", color ="#e0284a", image = "i_he", callback = name_callback, cb_name = "hel", window_background = "textboxx.png", who_outlines=[(1, "#000000", 0, 0)])
define ad = Character("Adara", color ="#58D3E3", image = "i_ad", callback = name_callback, cb_name = "ada", window_background = "textboxx.png")
define ho = Character("Hortensia", color ="#da7b00", image = "i_ho", callback = name_callback, cb_name = "hor", window_background = "textboxx.png")
define ch = Character("[cerdo]", color ="#FF9DBA", window_background = "textboxx.png")
define hu = Character("Hugo", color ="#5adbff",  image = "i_hu", callback = name_callback, cb_name = "hug", window_background = "textboxx.png")
define ac = Character("Atencion al cliente", color ="#61B3C9", window_background = "textboxx.png")
define co = Character("%#!#%!?#!%", color ="#888888", window_background = "textboxx.png")
define el = Character("Elodia Rivas", color ="#61B3C9", image = "i_el", callback = name_callback, cb_name = "elo", window_background = "textboxx.png")
define s1 = Character("Secuaz", color ="#61B3C9", window_background = "textboxx.png")
define s2 = Character("Secuaz", color ="#947a7a", window_background = "textboxx.png")
define ma = Character("Mujer", color = "#61B3C9", window_background = "textboxx.png")
define n = Character("", what_outlines=[( 1, "#000000", 0, 0 )])
define nvle = Character("", color="#ffffff", kind=nvl)

##### Declaración de flags de rutas
default principal_flag = True
default novias_flag = False
default coqueteo_flag = False
default flash_flag = False
default secuestro_flag = False
default salvar_flag = False
default caminoa_flag = False
default caminob_flag = False
default ui_novias_in = True
default ui_secuestro_in = True

##### Declaración de variables
default contacto_contador = 0
default cerdo = "Cerdo"
default draggable = False
default droppable = False
default persistent.audio_cues = ""
default user_input = ""
define correct_password = "24H-0325-7A"
default userr_input = ""
define correct_clave = "EXP-SAFJA"

default mama = True
default chancho = True
default dijo = True

default final_arbol = False

define _scene_show_hide_transition = Dissolve(0.25)

label splashscreen:
    $ renpy.movie_cutscene('splash.ogv')
    return

###### El juego ####################################################################
####################################################################################
label start:
    stop music
    
    show warning
    show control atl transitions at controlposition 
    ""

    label inicioUI_label:
        $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)
        hide screen arbol_screen
        $ principal_flag = True
        $ novias_flag = False
        $ coqueteo_flag = False
        $ flash_flag = False
        $ secuestro_flag = False
        $ salvar_flag = False
        $ caminoa_flag = False
        $ caminob_flag = False


    scene black


    ###### Flash Ella te odió ############################
    #################################################
    
    play music "audio/Un Inicio crudo.wav"
    show carneVelas with fade1
    nvl clear
    nvle ""
    hide control
    
    ma "Por favor..."

    image control atl transitions:
        "mouse.png" 
        pause 0.9
        "barra.png" 
        pause 0.9
        repeat

    scene bg senora
    nvl clear
    ma "...dime si ella me perdonó, ¡Te lo suplico!"
    
    
    show papas
    voice "Hugo1.mp3"
    hu "Vamos mi niña, solo tienes que probar un poco, ¿o es que no quieres ayudar a esta pobre mujer?"
    
    voice "mama1.mp3"
    ho "Hugo, no la presiones."
    voice "Hugo2.mp3"
    hu "Tienes razón, confío en que nuestra chica buena hará lo correcto como siempre, ¿verdad, Lena?"
    voice "N355.mp3"
    nvle "La carne gotea, manchándole la ropa. Helena la observa, con asco."
    
    scene bg boca
    nvl clear 
    voice "N356.mp3"
    nvle "No obstante, la pequeña cierra los ojos, respira profundo y, finalmente, le da un mordisco al trozo de carne."
    nvl clear 
    show fbojos with fade
    play sound "audio/creppy.mp3"
    voice "N357.mp3"
    nvle "El mundo a su alrededor se desvanece."
    ""

    scene black with fade1
    nvl clear
    stop music
    $ renpy.movie_cutscene("insolacion.ogv", stop_music=True) # Esto hace que el video se reproduzca en pantalla y se espere hasta que termine
    
    scene bg senora with fade
    nvl clear
    play music "audio/AntesQueTodo.ogg"
    
    voice "Nina_2.mp3" 
    he "Ella... te odió hasta su último aliento."
    play sound "audio/Ambientacion/IN 1.mp3"


    ###### Funeral ##################################
    #################################################
    scene bg hoyo with fade1 
    nvl clear 
    voice "N358.mp3"
    nvle "Helena se detiene al contemplar un agujero en la tierra.."
    scene bg charco
    nvl clear
    voice "N359.mp3"
    nvle "Observa las gotas de lluvia caer a sus pies."

    scene black with dissolve
    # TRACK 1 MA-MA
    $ renpy.movie_cutscene("Song1.ogv", stop_music=True) #Audio
    
    scene bg ramoflores
    nvl clear 
    voice "N360.mp3"
    nvle "Se limita a cerrar los ojos, como si estuviera orando, y a recitar algunas palabras."
    #TRACK 1
    voice "Helena_3.mp3" 
    he "Si no estás aquí, ¿dónde te encuentro?"
    scene bg charco
    nvl clear 
    voice "N361.mp3"
    nvle "La muchacha con el pelo empapado se pone en cuclillas para colocar el arreglo floral a la cabeza del agujero."
    scene bg funeral hoyo
    nvl clear 
    voice "N362.mp3"
    nvle "Toma la pala y duda si irse."
    scene black
    nvl clear
    if persistent.audio_cues:
        $ Descripcion = "Canción interpretada por Helena"
   
    $ renpy.movie_cutscene("celular.ogv", stop_music=False) # Esto hace que el video se reproduzca en pantalla y se espere hasta que termine

    scene bg funeral hoyo
    nvl clear 
    voice "N363.mp3"
    nvle "Finalmente, ya más calmada, se retira del lugar, dirigiéndose a una zona más poblada que se vislumbra a la lejanía."
    show cerdos
    voice "N364.mp3"
    nvle "Un grupo de cerdos se acerca, uno de ellos se queda mirando en la dirección por dónde salió Helena."
    voice "N365.mp3"
    nvle "El grupo detiene su caminata junto al agujero."
    voice "N366.mp3"
    nvle "El cerdo gira la cabeza para husmear qué hay al fondo del hoyo. No obstante, parece que no hay nada."
    voice "N367.mp3"
    nvle "Los cerdos continúan su camino. El cerdo comienza a seguir la misma ruta que Helena."
    nvl clear


    ###### Super ####################################
    #################################################
    if persistent.audio_cues:
        $ Descripcion = ""
    
    scene bg super
    nvl clear
    voice "N368.mp3"
    nvle "En la zona más habitada del pueblo."
    voice "N369.mp3"
    nvle "Junto a la entrada del supermercado, una madre junto a un par de niños piden limosna."
    voice "N370.mp3"
    nvle "Cuando Helena pasa junto a ellos, la mujer le pide una limosna, mugidos se le escapan cada tanto mientras trata de comunicarse."
    nvl clear

    #Interacción Super
    stop music
    play sound "audio/puertaMercado.mp3"
    play sound "audio/multitud.mp3" #AudioCue
    scene bg pasillo
    nvl clear
    if persistent.audio_cues:
        $ Descripcion = "Se escucha una multitud"

    voice "N371.mp3"
    nvle "La joven avanza con pasos constantes pero inseguros y busca con la mirada el pasillo al que debería dirigirse. "
    
    show screen anaquel_screen
    voice "N372.mp3"
    nvl clear
    nvle "Ve a la sección de carnes."

    label anaquel_label:
        hide screen anaquel_screen


    ###### INTERACCIÓN CUPON #######################
    ################################################

    scene bg elevador
    nvl clear
    show screen cupon_screen
    if persistent.audio_cues:
        $ Descripcion = ""

    "Aquí puedo verificar mi cupón"

    label cupon_label:
            hide screen cupon_screen

    scene bg maquina
    nvl clear
    call screen drag_sample2
    show screen drag_sample3
    if droppable == "The Left Circle":
        $ xpos_var = 150
    else:
        $ xpos_var = 640
    if draggable == "circle":
        show maquina on
        play sound "audio/MaquinaOn.mp3"
    
    ################################################
    ################################################
    nvl clear
    
    nvle "Cupón escaneado"
    
    scene bg congelador
    nvl clear
    play sound "audio/puertaMercado.mp3"
    voice "N373.mp3"
    "Oferta de carne" "Enfermedad terminal."
    voice "N374.mp3"
    "Oferta de carne" "Muerte brutal que dejó sus restos en muy mal estado." 
    voice "N375.mp3"
    "Oferta de carne " "Edad avanzada."
    scene bg congelador_blur
    nvl clear
    show screen refri_screen
    "Oferta de carne" "Tatuajes o arreglos estéticos que pueden afectar el sabor."
    ##### Interacción Refri
    label refrifake_label:
        voice "N377.mp3"
        "Aquí no está."
            
    label refri_label:
        hide screen refri_screen with dissolve
    
    nvl clear
    voice "N378.mp3"
    nvle "Helena se frota los brazos con las manos mientras avanza. El lugar es extremadamente helado."
    voice "N379.mp3"
    nvle "Se detiene en seco, con los ojos bien abiertos. Los dedos le tiemblan un poco, su respiración también lo hace."
    
    voice "N380.mp3"
    nvle "Sus dedos chocan con la mano de alguien más."  
    voice "N381.mp3"
    nvle "Se gira para ver a quién le pertenece la mano, y le sorprende ver de quién se trata."
    
    hide helena
    show i_he_tres at leftdialogue with easeinleft
    
    voice "Helena_4.mp3" 
    he "¡¿Te querías comer a mi mamá?!"
    
    show i_ad_tres at right with easeinright

    voice "Adara_01.mp3" 
    ad "¿Tan mala idea tienes de mí, Lena?"
    nvl clear
    ##### Decision
    menu: 
        nvle "Helena:"
        "No entiendo por qué sigues aquí":
            #voice "Helena_50.mp3"
            he "No entiendo por qué sigues aquí"

        "Dime qué haces aquí":
            voice "Helena_50.mp3"
            he "Dime qué haces aquí"
    
    voice "Adara_02.mp3" 
    ad "Ya sabes, como tienes problemas con esto de la carne, creí... no sé, pensé que quizás no ibas a querer saber nada de los restos de Hortensia."
    voice "N378.mp3"
    voice "N382.mp3"
    nvl clear
    nvle "Helena mira la bandeja, la toma con lentitud y Adara termina soltándola."
    voice "Helena_5.mp3" 
    hide i_he_tres
    hide i_ad_tres
    show i_he_espalda at leftdialogue
    show i_ad_frente at right
    he "Es mi mamá, o por lo menos lo que queda de ella. Prefiero que esto se quede conmigo a que acabe servido en la mesa de algún extraño."
    voice "Adara_03.mp3" 
    ad "Yo no soy una extraña, Hortensia también era importante para mí."
    voice "N379.mp3"
    voice "N383.mp3"
    nvl clear
    nvle "Helena se mantiene en silencio sin voltearla a ver."
    voice"Adara_04.mp3" 
    ad "Perdón, debí preguntarte antes de venir en lugar de asumir las cosas."
    ad "Yo tampoco quería que su cuerpo terminara como una cena más o algo así. Y... lamento mucho lo que le pasó, fue algo... inesperado."
    voice "Helena_6.mp3" 
    he "Si fue inesperado para ti que trabajabas con ella, imagina qué tan inesperado fue para mí."
    voice "N384.mp3"
    nvl clear
    nvle "Toma otras dos charolas del mismo lote, el lote de su madre."
    
    voice"Adara_05.mp3" 
    ad "Helena, yo no estaba con Hortensia cuando sucedió el accidente, \nni siquiera me dejaron verla luego de que me enteré de que le había pasado algo."
    voice "N385.mp3"
    nvl clear
    nvle "Helena ignora a la rubia"
    
    voice "Adara_06.mp3" 
    ad "No me crees, ¿verdad?"
    
    voice "Helena_7.mp3" 
    he "¿Debería hacerlo?"
    voice "N386.mp3"
    nvl clear
    nvle "Adara abre la boca, mas no sale palabra de ella. Ante esto, Helena se gira, dispuesta a salir por donde llegó."

    scene bg mercado psico with fade
    nvl clear
    voice "Adara_07.mp3" 
    ad "Lena, espera, por favor."
    voice "N387.mp3"
    nvle "Helena se detiene frente a ella."
    
    voice "Adara_08.mp3" 
    ad "Sobre lo otro que pasó, ya no soy así y yo no..."
    voice "Helena_8.mp3" 
    he "Este no es el momento para hablar de eso."
    voice "Adara_09.mp3" 
    ad "Pero en serio quiero que arreglemos las cosas..."
    voice "Helena_9.mp3" 
    he "Pues yo no."
    voice "Helena_10.mp3" 
    he "Si de verdad querías arreglar las cosas, pudiste haber empezado siendo la primera en avisarme lo de mi mamá."
    scene black
    nvl clear
    voice "N388.mp3"
    nvle "Helena regresa la vista al frente y se retira del lugar. Adara, por su parte, suelta un suspiro y se queda en donde está."
    

    ###### Sospecha #################################
    #################################################
    scene bg casa with fade1
    nvl clear
    voice "N389.mp3"
    nvle "Helena observa las charolas de carne con una mirada fría y afligida. "
    scene bg sillon
    nvl clear
    voice "N390.mp3"
    nvle "La chica entra a la casa. Se deja caer sobre el sofá principal."
    scene bg mesa
    nvl clear
    voice "N391.mp3"
    nvle "Helena observa las charolas de carne con una mirada fría y afligida."
    voice "N392.mp3"
    nvle "Un par de arcadas la atacan."
    scene bg carne
    nvl clear
    voice "Helena_11.mp3" 
    he "Así que te convirtieron en esto..."
    voice "Helena_13.mp3" 
    he "Hoy es 12 de mayo, y mi mamá falleció hace 4 días, el 8 de mayo. Creo que la fecha de procesamiento está mal..."
    "La joven revisa las etiquetas de las otras charolas, y se percata de que la fecha de procesamiento también es incorrecta en ambas."
    "Le da vueltas al extraño error durante algunos minutos, y termina tomando la decisión de marcar al número de atención al consumidor para reportar el error."

    scene black with dissolve
    nvl clear
    if persistent.audio_cues:
        $ Descripcion = "Se escucha un celular llamando"
    show CelularDos
    voice "ac1.mp3"
    ac "Atención al cliente de Novacárnicos, ¿en qué puedo servirle?"
    voice "Helena_14.mp3" 
    he "Buenas tardes, llamo para reportar un error en la fecha de procesamiento de un lote."
    voice "ac2.mp3"
    ac "Si fuera tan amable de proporcionarme el código del lote."
    
    if persistent.audio_cues:
        $ Descripcion = ""

    scene bg carneclose
    nvl clear
    label input_label:
        $ user_input = renpy.input("El lote es...")
        if user_input == correct_password:
            voice "Helena_15.mp3" 
            play sound "audio/Foley/Escribir en el teclado.mp3"
            voice "ac3.mp3"
            ac "Espere un momento por favor... Le confirmo la información del lote: Lote 24H-0325-7A, procedente de Verónica Pérez Ramírez, ¿es correcto?"
    
        else:
            voice "ac11.mp3"
            ac "No hay ningún lote con ese código."
            jump input_label
 
    voice "Helena_16.mp3" 
    he "No, no, no, ehhh...la persona, el nombre de la persona también está mal. El lote es de Hortensia González Serrano."
    play sound "ac4.mp3"
    ac "No señorita, aquí dice que el código de lote que me proporcionó, pertenece a Verónica Pérez Ramírez, con fecha de procesamiento del 8 de mayo."
    ac "Certificado 'Sana y Fuerte' aprobado, individuo en óptimo estado de salud antes del procesamiento,"
    ac "sin historial de enfermedades degenerativas, alimentación balanceada y nivel de actividad física adecuado. ¿Estoy en lo correcto?"
    stop sound
    voice "Helena_17.mp3" 
    he "Ehhh... sí, los datos de la fuente están bien, pero lo demás no, le repito:"
    he "La mujer se llama Hortensia González Serrano, y la fecha de procesamiento debería ser el 8 de mayo."
    
    show CelularDos with fade3
    play sound "ac5.mp3"
    ac "Según la información que me arroja el sistema, no hay registro de que ninguna Hortensia González Serrano haya sido procesada,"
    ac "ni en esta ni en ninguna otra planta correspondiente a Novacárnicos."
    stop sound
    he ""
    voice "ac6.mp3"
    ac "¿Continúa al otro lado de la línea, señorita?"
    voice "Helena_18.mp3" 
    he "¿Y si lo intenta de nuevo? Es Hortensia con 'h', González con acento en la 'a' y 'z' al final, y Serrano con..."
    play sound "ac7.mp3"
    ac "Con 's' al inicio y doble 'r', sí sé escribir, señorita."
    ac " Como le comentaba, no hay registro de que ese cuerpo haya sido procesado con nosotros, ¿le puedo ayudar con algo más?"
    stop sound
    voice "Helena_19.mp3" 
    he "Debe haber un error, ¿y si intenta..."
    play sound "ac8.mp3"
    ac "En estos últimos 20 años, desde la propagación del virus MA y posterior legalización de la necrofagia, nuestro sistema nunca,"
    ac "Jamás, ha presentado ni el más mínimo fallo, por lo que puede estar segura de que la información que le proporcioné es correcta."
    ac "Ahora, dígame, ¿le puedo ayudar con algo más?"
    stop sound
    voice "N393.mp3"
    nvle "El corazón de Helena se acelera, su pecho sube y baja aumentando cada vez más la velocidad."
    voice "ac10.mp3"
    ac "¿Señorita?, ¿le puedo ayudar...?"
    voice "Helena_20.mp3" 
    he "No, con eso es suficiente."
    voice "N394.mp3"
    nvle "Helena cuelga."

    scene bg sillon blur with dissolve
    nvl clear
    show i_he_decadencia at center
    play sound "Helena_21.mp3" 
    he "No entiendo qué está pasando,{p=1.5}no entiendo nada...{p=1.5}ojalá estuvieras aquí..."
    he "ojalá pudiera saber... {p=1.5} te extraño tanto."


    ###### Flash ya no ##############################
    #################################################
    play sound "audio/Ambientacion/IN 1.mp3"
    show fbtormento with fade1
    voice "Nina_3.mp3" 
    he "Ya no quiero... no quiero más."
    
    voice "Nina_4.mp3" 
    he "No quiero comerla..."
    voice "Nina_6.mp3" 
    he "... no quiero tocarla..."
    voice "Nina_7.mp3" 
    he "... no quiero ser esto."
    #voice "N394.mp3"
    nvle "Su madre la observa y escucha con atención, con una expresión arrepentida, culpable."
    voice "Nina_8.mp3" 
    he "¿Nací para ser esto?"
    show hortensia at leftdialogue
    voice "N395.mp3"
    nvle "Ante la pregunta, Hortensia se queda en silencio. Abraza a su hija con más fuerza contra su pecho."
    voice "mama2.mp3"
    ho "Está bien, hija."
    voice "mama3.mp3"
    ho "Si eso es lo que quieres, está bien."
    show hugo lateral at right
    voice "Hugo3.mp3"
    hu "¿Así que quieres dejar de comer carne? Pues muérete de hambre."
    voice "N396.mp3"
    nvle "Hortensia mira a Hugo con desprecio y trata de cubrir más a la pequeña con sus brazos."
    voice "Nina_9.mp3" 
    he "Prefiero eso."
    play sound "audio/Ambientacion/IN 1.mp3"

    ###### ¿PRUEBO la carne? ########################
    #################################################
    #scene bg mesa with dissolve
    show pruebaCarne with fade1
    voice "N397.mp3"
    nvle "La chica toma uno de los paquetes, le quita el plástico y saca un trozo de carne con lentitud, agarrándolo solo con la punta de los dedos."

    voice "N398.mp3"
    nvle "Lo contempla con repulsión, más comienza a acercarlo a su boca."
    $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)

    ##### PRUEBO Decision############################
    menu: 
        nvle "¿Pruebo la carne?"
        "No puedo creer que voy a hacer esto de nuevo.":
            
            he "No puedo creer que voy a hacer esto de nuevo."

        "No quiero comerla...":
            voice "Helena_70.mp3"
            he "No quiero comerla..."
            jump chancho #Jump porque es final, y no volvemos
    ###### PRUEBO 

    voice "N399.mp3"
    nvle "Helena cierra los ojos con fuerza y, sin pensarlo más, le da un mordisco a la carne y se lo pasa."
    voice "N400.mp3"
    nvle "Se cubre la boca con una mano cuando la carne amenaza con salir."
    voice "N401.mp3"
    nvle "Y entonces... nada."
    voice "Helena_23.mp3" 
    he "Tal vez necesito comer un poco más..."

    show fbojos
    play sound "N402.mp3"
    nvle "Sin previo aviso, las extremidades del cuerpo de Helena se tensan tanto que comienzan a tiritar"
    nvle "sus manos se hacen puños, su espalda se arquea, su cabeza se echa para atrás, sus ojos se tornan totalmente rosados, casi rojizos"
    stop sound
    voice "N403.mp3"
    play sound "audio/Foley/Rechinido.mp3"
    nvle " y sus dientes ejercen fuerza los unos sobre los otros, emitiendo un rechinido que se siente solo de escucharlo."

    show FB_suicidio with fade1
    if persistent.audio_cues:
        $ Descripcion = "Se escucha una cuerda tensa"
    ""
    if persistent.audio_cues:
        $ Descripcion = ""
    scene bg vomito with fade1
    nvl clear
    voice "N404.mp3"
    nvle "De golpe, Helena abre los ojos, jadeante, volviendo al momento presente, a su cuerpo, a su realidad."
    voice "N405.mp3"
    nvle "Está agitada y gotas de sudor le corren por la frente."
    
    #scene bg almas
    
    voice "Helena_24.mp3" 
    he "Ay, hace tanto que no sentía esto, es tan... doloroso."

    show almas
    voice "Helena_25.mp3" 
    he "Pero es incluso más doloroso saber que tú no eres mi mamá."
    scene black
    nvl clear
    voice "N406.mp3"
    nvle "Helena se levanta del sillón y sale de la casa." #, y se va a otra habitación."
    
    ###### Se da cuenta #############################
    #################################################
    
    scene bg pasillo
    nvl clear
    voice "N407.mp3"
    nvle "Helena se apresura a llegar al pasillo en donde estaban los restos de su madre."
    scene bg refri carne
    nvl clear
    voice "Helena_27.mp3" 
    he "Los paquetes que estaban cerca del de mi mamá no sólo fueron procesados por la misma empresa{p=1.5}sino que también tienen fechas de procesamiento cercanas. Si su carne está en algún lado, tiene que ser ahí."
    voice "N408.mp3"
    nvle "La castaña toma una charola de cada lote que sospecha que podría corresponder en realidad al de su madre. Apila los paquetes como puede, uno sobre otro."
    scene black
    nvl clear
    voice "N409.mp3"
    nvle "Compra todos los que puede."
    
    ###### vomita ###################################
    #################################################
    $ ui_nota = True
    label notaUI_label:
        hide screen arbol_screen
        $ principal_flag = True
        $ novias_flag = False
        $ coqueteo_flag = False
        $ flash_flag = False
        $ secuestro_flag = False
        $ salvar_flag = False
        $ caminoa_flag = False
        $ caminob_flag = False

    scene bg casa with dissolve
    nvl clear
    voice "N410.mp3"
    nvle "Helena entra a la cocina cargando varias bolsas."
    scene bg carnes
    nvl clear
    voice "Helena_28.mp3" 
    he "Te voy a encontrar."
    voice "N411.mp3"
    "Toma un paquete de carne al azar y lo abre velozmente. Saca un pedazo de carne, lo muerde y se lo traga a regañadientes. Y el mundo a su alrededor se desvanece. "
    
    show almas
    voice "N412.mp3"
    "Helena ve imágenes fugaces."
    voice "N413.mp3"
    "El proceso se repite una y otra vez y, con cada trozo de carne consumido"
    voice "N414.mp3"
    "Ninguno es la mamá de Helena."
    
    scene bg casa
    nvl clear
    show helena decadencia at center with slow_dissolve
    voice "Helena_29.mp3"
    he "Solo nombres. Solo muertes. Solo historias que no son la tuya."
    he "¿Cuántos más, mamá?, ¿cuántos más tengo que tragarme para encontrarte?"
    voice "N415.mp3"
    nvle "Helena se talla la boca , para limpiarse los restos de sangre"
    voice "N416.mp3"
    nvle "Se escuchan ruidos extraños afuera y decide ir a inspeccionar."

    scene bg casa exterior with fade
    nvl clear
    voice "N417.mp3"
    nvle "Helena sale de la casa, extrañada, y busca con la mirada el origen del ruido."
    show chancho sentado at left with easeinleft
    voice "N418.mp3"
    nvle "Macetas destrozadas, tierra regada por el piso, flores arrancadas marchitándose y un cerdo en el center de todo, con una flor de caléndula en el hocico."
    show helena tress at right with easeinright
    voice "Helena_30.mp3" 
    he "¡Maldito puerco, deja ahí!"
    voice "N419.mp3"
    nvle "El cerdo voltea a ver a Helena, todavía masticando la flor."
    voice "N420.mp3"
    nvle "La chica camina hacia el puerco y trata de mover de lugar la maceta de caléndulas."
    hide chancho sentado
    show chancho at left with dissolve
    voice "N421.mp3"
    nvle "Sin embargo, el cerdo se levanta en sus patas traseras y agarra la maceta con las pezuñas. "
    voice "Helena_31.mp3" 
    he "¡¿Un fracturado?!, ¿cómo llegó hasta aquí?"
    if persistent.audio_cues:
        $ Descripcion = "Se escuchan chillidos del cerdo"
    voice "N422.mp3"
    nvle "Forcejean. El cerdo comienza a chillar, lo cual irrita más a la muchacha."
    voice "N423.mp3"
    nvle "El cerdo sigue chillando, pero no trata de seguirla. Helena entra a su casa."
    if persistent.audio_cues:
        $ Descripcion = ""


    ###### Lee la nota ##############################
    #################################################
    scene bg casa
    nvl clear
    show helena lateral at right with easeinright
    
    voice "N424.mp3"
    nvle "Pone la maceta, con algo de brusquedad, sobre la encimera de la cocina, junto a una ventana."
    voice "N425.mp3"
    nvle "La chica busca una bolsa de basura y, cuando la tiene, comienza a meter dentro de ella todos los desechos que quedaron de las bandejas de carne que probó."
    voice "N426.mp3"
    nvle "Deja la bolsa por un lado, y ahora recoge los paquetes que siguen intactos, los que ni siquiera abrió."
    voice "N427.mp3"
    play sound "audio/Foley/Bandeja cayendo.mp3"
    nvle "Helena mete las bandejas con descuido al refrigerador, empujandolas hasta el fondo para que quepan todas."
    voice "N428.mp3"
    nvle "Finalmente, cierra la puerta con fuerza, provocando que varios imanes, tickets y demás papeles, que estaban adheridos caigan al suelo."
    scene bg cosas suelo 
    nvl clear
    voice "Helena_32.mp3" 
    he "¡Ahg!, ¡lo que me faltaba! Por si el día no se podía poner peor."

    scene bg cosas suelo with dissolve
    nvl clear
    voice "N429.mp3"
    nvle "Helena se apresura a recoger las cosas. Imanes, tickets de compras, postales, una nota extraña..."
    voice "Helena_33.mp3" 
    he "No puede ser. Es la letra de mi mamá."
    voice "N430.mp3"
    nvle "Se pone de pie velozmente y deja todas las cosas que tomó del piso sobre la encimera, quedándose únicamente con la nota, en la cual se lee:"
    play sound "mama4.mp3"
    ho "¿Recuerdas cuando fuimos de campamento al bosque? Fue un día maravilloso, te veías tan adorable en la foto que te tomé ese día. ¿Deberíamos ir de nuevo?"
    play sound "Helena_34.mp3" 
    he "¿Es todo? Pero... ¿qué quería decir? Si ese día fue horrible nos picaron los insectos, olvidamos la casa de campaña,"
    he "llovió durante toda la noche, se nos terminó el agua... ella también odió ese día."
    stop sound
    voice "N431.mp3"
    nvle "Helena se queda repasando lo que dice la nota durante un momento. Y, de la nada, parece que algo hace clic."
    scene black
    nvl clear
    voice "N432.mp3"
    nvle "La chica sale casi corriendo de la cocina, en dirección a una habitación."
    
    scene bg hortensia with fade3
    nvl clear
    if persistent.audio_cues:
        $ Descripcion = "Se escucha el abrir de una puerta"
    play sound "audio/puerta.mp3"
    voice "Helena_36.mp3" 
    he "No había entrado aquí desde lo que pasó. Se siente... extraño."
    if persistent.audio_cues:
        $ Descripcion = ""
    show screen cuarto_screen

    voice "Helena_35.mp3" 
    he "La foto, ¿dónde quedó esa foto?"
    
    label cuartofake_label:
        "Aquí no está."

    label cuarto_label:
        hide screen cuarto_screen
        voice "Helena_37.mp3" 
        he "Bingo."
        
    scene bg hortensia blur with dissolve
    nvl clear
    show CartaMama
    ""
    scene bg hortensia
    nvl clear
    voice "N433.mp3"
    nvle "Al terminar de leer la nota, Helena se sienta sobre la cama, confundida y con el ceño fruncido."
    scene bg hortensia blur with dissolve
    nvl clear
    show helena decadencia at center with slow_dissolve
    voice "Helena_38.mp3" 
    he "¿En qué te metiste para terminar así, mamá?"
    play sound "audio/Helena/Helena_38.mp3" 
    he "¿De verdad era algo tan importante para ti?"
    he "Y si así era, ¿por qué no me lo contaste?"
    stop sound
    voice "N434.mp3"
    nvle "Se guarda la foto en uno de los bolsillos de su ropa."
    
    voice "Helena_39.mp3" 
    he "Necesito respuestas, y si Adara las tiene... creo que no queda nada más que pensar. Tengo que ir a verla." 
    voice "Helena_78.mp3"
    he "Pero todavía estoy molesta y la verdad no la quiero volver a ver."

    ###### VOY Decision##############################
    voice "N435.mp3"
    menu: 
        
        nvle "¿Voy con Adara?"
        "No la quiero volver a ver.":
            $ flash_flag = True #Entro a la ruta flashbacks
            voice "Helena_89.mp3"
            he "No la quiero volver a ver."
            jump flash #jump porque no vuelvo

        "Tengo que ir a verla.":
            voice "Helena_100.mp3"
            he "Tengo que ir a verla."
    ##### VOY

    scene black
    nvl clear
    voice "N436.mp3"
    nvle "Helena se pone de pie y sale de la habitación."


    ###### casa de Adara ############################
    #################################################
    scene bg casa
    nvl clear
    show helena at left with slow_dissolve
    voice "N437.mp3"
    nvle "Helena pasa por la cocina, lista para seguir hasta la sala y salir de la casa, pero un ruido raro llama su atención."
    voice "N438.mp3"
    nvle "La ventana de la cocina está abierta y sobre la encimera, en donde antes solo estaba la maceta, se encuentra al cerdo comiéndose las flores de caléndula."
    scene bg ventana
    nvl clear
    voice "Helena_40.mp3" 
    he "¡Otra vez tú, marrano!"
    voice "N439.mp3"
    nvle "El cerdo gira para verla."
    ch "Oink, oink"
    voice "Helena_111.mp3"
    he "¡AGH!"
    show helena tress at right with easeinright
    voice "N440.mp3"
    nvle "Enfurecida, le quita la maltratada maceta, lo levanta con las manos, asegurándose de mantenerlo alejado del resto de su cuerpo, y lo carga hasta afuera de la casa."
    scene bg casa exterior
    nvl clear
    show chancho sentado 
    voice "N441.mp3"
    nvle "Helena deja al cerdo en el piso, para después limpiarse las manos. El cerdo se sienta y se le queda viendo con atención."
    voice "Helena_122.mp3"
    he "¿Contento? Ya echaste a perder mis flores, ¿ahora qué quieres?, ¿qué se te antoja?, ¿bugambilias?, ¿dientes de león?, ¿albahaca?"
    voice "N442.mp3"
    nvle "El cerdo se acerca a Helena y comienza a olerle los zapatos. Después de un momento, decide aferrarse a una de sus piernas."
    voice "N443.mp3"
    nvle "Helena lo observa, todavía más molesta, y empieza a agitar su pierna con violencia hasta que logra soltarse del agarre del cerdo."
    voice "Helena_133.mp3"
    he "Sabes qué, no me importa, puedes comerte lo que quieras, yo me voy."
    scene bg calle
    nvl clear
    voice "N444.mp3"
    nvle "La castaña se encamina a casa de Adara, pero escucha unos pequeños pasos siguiéndola. Mira hacia atrás, y nota al cerdo siguiéndola."
    show helena espalda at rightdialogue with dissolve
    voice "Helena_41.mp3"
    he "¡Shu, shu!"
    show chancho at leftdown with dissolve
    voice "N445.mp3"
    nvle "Su pobre intento no ahuyenta al animal, por lo que decide ignorarlo y continuar avanzando. El cerdo la sigue a unos metros de distancia."
    voice "Helena_51.mp3"
    he "No tengo tiempo para lidiar con esto."
    voice "N446.mp3"
    nvle "Helena y cerdo se dirigen a la casa de Adara."
   
    scene bg adara puerta with fade2
    nvl clear
    hide helena
    voice "N447.mp3"
    nvle "Helena está nerviosa y con los brazos cruzados al pecho y los hombros tensos, ignora que el pequeño cerdo se mantiene escalones abajo olfateando el jardín de la entrada."
    
    if persistent.audio_cues:
        $ Descripcion = "Se escucha un timbre"
    
    play sound "audio/knock knock.mp3"
    voice "N448.mp3"
    nvle "La joven timbra y espera mirando las plantas tan frescas que crecen en el pequeño jardín y en su cara surge una pequeña sonrisa. Hacen contacto visual en completo silencio."
    
    if persistent.audio_cues:
        $ Descripcion = ""
    scene bg adara puerta_blur with dissolve
    nvl clear
    
    show i_ad_tres at right with easeinright
    voice "Adara_10.mp3" 
    ad "Vaya, pensé que ya no querías volver a verme."
    voice "Helena_52.mp3"
    show i_he_tres at leftdialogue with easeinleft
    he "No te emociones, si vine es porque necesito respuestas... es sobre mi mamá."
    voice "N449.mp3"
    nvle "Helena ve de reojo que el puerco se acerca y con el ceño fruncido lo aparta con el pie. Adara duda un momento en dejarla pasar, respira hondo y abre por completo la puerta."
    scene bg adara casa
    nvl clear
    voice "N450.mp3"
    nvle "Helena se adentra en la casa, de repente Helena se percata de los pasitos del cerdo detrás de ella, molesta se voltea a verlo. Este rápidamente regresa a la entrada y se sienta de manera cohibida."
    
    show chancho chiqui at chiqui
    play sound "cerdo1.wav"
    voice "Helena_53.mp3"
    he "Ahh, Cerdo..."
    voice "N451.mp3"
    nvle "El cerdo bufa desde afuera cortando el tenso silencio que se forma en la sala. "
    scene bg adara casa_blur with dissolve
    nvl clear
    show i_ad_tres at right with easeinright
    voice "Adara_19.mp3" 
    ad "Bueno, dime, ¿qué pasó?"
    voice "Helena_56.mp3"
    show i_he_tres at leftdialogue with easeinleft
    he "Dicen que murió. Pero la carne... no era de ella."
    voice "Adara_20.mp3" 
    ad "¿Estás segura de eso?"
    voice "Helena_57.mp3"
    he "Sí. Ninguno de los paquetes eran de ella."
    voice "Adara_21.mp3" 
    ad "Oh la probaste..."
    
    voice "Adara_22.mp3" 
    ad "¿Y por qué vienes a mí ahora? Después de tanto tiempo."

    ##### Decision
    menu: 
        "Porque mi mamá confiaba en ti.":
            voice "Helena_58.mp3"
            he "Porque mi mamá confiaba en ti."

        "Porque... no tengo a nadie más.":
            voice "Helena_59.mp3"
            he "Porque... no tengo a nadie más."

    scene bg comida with fade
    nvl clear
    voice "N452.mp3"
    nvle "Adara suspira, se levanta y se da la vuelta para dirigirse a su cocina. Le deja unas verduras en la barra. "
    show i_ad_tres at right with dissolve
    voice "Adara_23.mp3" 
    ad "Ten, no eres tú misma ahorita, esto te ayudará."
    show i_he_tres at leftdialogue with dissolve
    voice "Helena_60.mp3"
    he "No tengo hambre"
    voice "Adara_24.mp3" 
    ad "Mmm okay, pero no te pregunté si tenías."

    he "Gracias, no tenías que preocuparte."
    ad "Disfruta"
    scene bg helena adara
    nvl clear
    voice "Adara_11.mp3" 
    ad "Estos últimos días noté que Hortensia actuaba un poco extraño, siempre estaba viendo a lo lejos o detrás de nosotras cuando íbamos arriba del camión... estaba algo paranoica, me decía que la tenían en la mira."
    voice "Helena_61.mp3"
    he "¿Quién? Nunca me contó nada."
    voice "Adara_12.mp3" 
    ad "No estaba segura. Me dijo que encontró algo... alguien muy importante, esas personas querían lo que encontró."
    voice "Helena_62.mp3"
    he "Pero entonces,"

    ##### Decision
    menu: 
        "¿Puede que mi mamá siga viva?":
            voice "Helena_63.mp3"
            he "¿Puede que mi mamá siga viva?"

        "¿Esas personas tienen que ver con la desaparición de mi mamá?":
            voice "Helena_64.mp3"
            he "¿Esas personas tienen que ver con la desaparición de mi mamá?"

    voice "Adara_13.mp3" 
    ad "Sí, seguramente."
    scene bg adara casa_blur with dissolve
    nvl clear
    voice "N453.mp3"
    nvle "Helena se levanta de su lugar abruptamente y mira a Adara con una expresión entre alivio y miedo."
    voice "Helena_65.mp3"
    he "¿En serio lo crees? Ahora todo tiene sentido."
    voice "Helena_66.mp3"
    he "Eso también significa que mi mamá está en peligro ¿no? Tengo que buscarla ya."
    voice "N454.mp3"
    nvle "Helena se da la vuelta para irse, pero Adara alcanza a tomarla del brazo y jalarla contra sí, deteniéndola en seco."
    voice "Adara_14.mp3" 
    ad "¡Lena! Tranquila, respira, sé que estás preocupada, pero primero debes pensar bien lo que vas a hacer, tú también pudieras estar en peligro."
    
    scene bg magenta with dissolve
    nvl clear
    show helena decadencia at centerleft with dissolve
    voice "N455.mp3"
    nvle "Helena empieza a hiperventilar y Adara termina abrazándola fuertemente. Helena siente como Adara le empieza a sobar la espalda y termina por calmarse contra su pecho, ahogando un grito."
    show adara frente at centerright behind helena with dissolve
    voice "Adara_15.mp3" 
    ad "Shhh... déjalo salir Helena, un día a la vez, pero ahora, ¿qué te parece si mejor comemos algo?"
    voice "N456.mp3"
    nvle "Helena se separa del cobijo de sus brazos, se talla la cara para limpiarse el rastro de su llanto mientras asiente."
    
    scene bg adara casa with dissolve
    nvl clear
    show i_he_tres at leftdialogue with dissolve
    voice "Helena_67.mp3"
    he "Vale, pero esto no significa que te voy a perdonar."
    show i_ad_tres at right with dissolve
    voice "Adara_16.mp3" 
    ad "Sí sí sí vente ándale."
    
    show chancho at center behind i_ad_tres with dissolve
    voice "N457.mp3"
    nvle "Helena termina comiendo frente a Adara, Adara le sirve una pequeña calabaza al cerdo dejándolo pasar al comedor."
    
    ##### Decision
    menu: 
        "Creí que no volvería a verte.":
            voice "Helena_68.mp3"
            he "Creí que no volvería a verte."
            voice "Adara_25.mp3"
            ad "Yo también lo pensé."

        "¿Y cómo has estado?":
            voice "Helena_69.mp3"
            he "¿Y cómo has estado?"
            ad "Bien, aprendí a cocinar."

    voice "N458.mp3"
    nvle "Helena sigue meneando su comida sin mucho ánimo."
    voice "Helena_71.mp3"
    he "Está muy rico."
    voice "Adara_27.mp3"
    ad "Aún haces esa cara cuando pruebas algo salado."
    voice "Helena_72.mp3"
    he "No sabía que lo notabas."
    voice "N459.mp3"
    nvle "Se miran la una a la otra, Adara se cruza de brazos y se acerca a Helena recargando sus codos en la barra. Discretamente Helena admira los brazos tonificados de Adara y se tapa la boca con la otra mano para disimular su sonrisa."
    voice "N460.mp3"
    nvle "Adara se da cuenta de la mirada curiosa de Helena, pero su momento es interrumpido por un ruido proveniente del jardín."
    
    ch "Oink oink oink"


    ###### ¿Duermo con Adara? ###################################
    #################################################
    voice "Adara_29.mp3"
    ad "Si vas a investigar mañana temprano, es mejor que descanses aquí."
    voice "N461.mp3"
    nvle "Adara la voltea a ver con una ceja levantada."
    voice "Adara_30.mp3"
    ad "Ay, sabes que no lo decía con esa intención."
    voice "Helena_73.mp3"
    he "Bueno, pero ¿estás segura?"
    voice "Adara_31.mp3"
    ad "No pienso echarlos, además...ya viste que aquí siguen estando tus cosas, puedes dormir en el cuarto si así lo deseas."
    
    ###### DUERMO Decision###########################
    menu: 
        "Ese ya no es mi cuarto.":
            $ novias_flag = False #Entro a la ruta Adara
            $ coqueteo_flag = False
            $ principal_flag = True
            $ secuestro_flag = True
            voice "Helena_74.mp3"
            he "Ese ya no es mi cuarto."
            voice "Helena_75.mp3"
            he "El puerco va a dormir afuera. Yo dormiré en el sillón, gracias y buenas noches."
            #jump pruebo_si

        "¿Contigo?":
            $ novias_flag = True #Entro a la ruta Adara
            $ coqueteo_flag = True
            $ principal_flag = False
            $ secuestro_flag = False #Me salí de la ruta principal
            voice "Helena_76.mp3"
            he "¿Contigo?"
            voice "Adara_32.mp3"
            ad "Sí."
            voice "Helena_77.mp3"
            he "Pues sí podría dormir arriba, hoy no tuve un buen día."
            voice "Helena_79.mp3"
            he "El puerco va a dormir afuera."
    ###### DUERMO

    ch "Oiiiiink"

    if principal_flag:
        scene bg adara casa_blur
        nvl clear
        voice "N462.mp3"
        nvle "Helena se acomoda en el sillón y se da la vuelta escondiendo su cara contra el respaldo, Adara se despide del cerdo para tranquilizarlo y se va a su cuarto. El cerdo se acuesta afuera de la casa. En realidad, nadie duerme del todo bien esa noche."

    if novias_flag:
        scene bg cama
        nvl clear
        voice "N463.mp3"
        nvle "Adara se despide del cerdo para tranquilizarlo y Helena entra a la habitación de Adara. El cerdo se acuesta afuera de la casa. En realidad, nadie duerme del todo bien esa noche."
    
    
    scene bg adara casa with fade1
    nvl clear
    voice "N464.mp3"
    nvle "Apenas se asoman los primeros rayos de sol por la ventana de la sala que da al jardín, el cerdo rasca la puerta de la entrada. "

    show i_ad_tres at right with easeinright

    if novias_flag:
        
        voice "Adara_33.mp3"
        ad "Ya extrañaba dormir contigo."
        show i_he_tres at leftdialogue with easeinleft
        voice "Helena_80.mp3"
        he "Adara, estaba muy mal ayer, no empieces, además no pasó nada."
        voice "Adara_34.mp3"
        ad "Está bien, no te preocupes."

    if principal_flag:
        voice "N465.mp3"
        nvle "Adara sale bostezando de su habitación. Adara le abre la puerta al cerdo."
        
        voice "Adara_35.mp3"
        ad "¿Mala noche?"
        show i_he_tres at leftdialogue with easeinleft
        voice "Helena_81.mp3"
        he "¿La tuya no?"
    
    show chancho at center behind i_ad_tres with dissolve
    voice "Adara_36.mp3"
    ad "Bueno, ¿y cómo fue que..."
    voice "N466.mp3"
    nvle "Adara apunta al cerdo, quién se ofende y sale al jardín."
    hide chancho
    voice "Helena_82.mp3"
    he "No sé, me sigue desde hace días."
    voice "Adara_37.mp3"
    ad "Pero ¿por qué?, ¿qué hiciste? Pensé que te causaban repulsión."
    voice "Helena_83.mp3"
    he "Pues ya ves. Pongamosle un nombre, ¿qué tal Chancho?."
    voice "Adara_38.mp3"
    ad "Me parece bien."
    voice "N467.mp3"
    nvle "Helena se levanta del sillón para estirarse. Adara se mete a la cocina y se pone a preparar el desayuno, Chancho entra."
    define chancho = "Chancho"
    show chancho at center behind i_ad_tres with dissolve
    voice "Adara_39.mp3"
    ad "¡Anda despierta! Ya sé quién puede ayudarnos."

    ###### Contacto #################################
    #################################################
    $ ui_contacto = True
    
    label contactoUI_label:
        $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)
        hide screen arbol_screen
        $ flash_flag = False
        $ salvar_flag = False
        $ caminoa_flag = False
        $ caminob_flag = False



    scene bg calle with fade3
    nvl clear
    voice "N468.mp3"
    nvle "El cielo está nublado. Helena, Adara y Chancho caminan por una calle olvidada, donde el concreto está agrietado y las paredes están cubiertas de grafitis descoloridos."
    voice "N469.mp3"
    nvle "Los únicos sonidos son los del viento y los pasos del trío. Chancho olfatea al aire preocupado."
    scene bg contacto with fade3
    nvl clear
    $ mama = True
    $ chancho = True
    $ dije = True
    show i_he_tres at leftdialogue with easeinleft
    
    voice "Helena_84.mp3"
    he "¿Con quién vamos?"
    show i_ad_tres at right with easeinright
    ad "Es un colega que Hortensia y yo conocimos, solía contar historias locas. Ella nunca le perdió el contacto."
    voice "N470.mp3"
    nvle "El cerdo se muestra inquieto desde que entraron a la zona. Sus orejas se mueven en todas direcciones. No se despega de Helena ni por un segundo."
    voice "N471.mp3"
    nvle "Adara los lleva hasta una estructura que parece más una bodega blindada que una vivienda. Hay una sensación extraña en el aire. Adara golpea la puerta principal con firmeza."
    voice "N472.mp3"
    nvle "Silencio... {p=1.5} Vuelve a golpear. Esta vez con un ritmo específico."
    
    ##### Interacción rejilla
    voice "N473.mp3"
    nvle "Un momento después, una rendija metálica se desliza desde dentro. Unos ojos hundidos y oscuros los observan desde el otro lado."
    voice "Contacto_01.mp3" 
    co "Dije que no iba a hablar con nadie más."
    voice "Adara_41.mp3"
    ad "No soy nadie más. Ábreme. Es sobre Hortensia."
    scene black with dissolve
    nvl clear
    voice "N474.mp3"
    nvle "Silencio. {p=1.5} Adara entra primero. Luego Helena, y Chancho."
    
    play sound "audio/puertaMetal.mp3"

    show contacto_video 
    voice "Contacto_02.mp3" 
    co "Ustedes no deberían estar aquí."
    voice "Helena_85.mp3"
    he "Queremos saber qué pasó con mi madre."
    show chancho sentado at leftdown with dissolve
    voice "N475.mp3"
    nvle "Sus ojos se desvían hacia Chancho. Lo examina con detenimiento."
    

    voice "Contacto_03.mp3" 
    co "Así que es cierto... el cerdito existe."
    voice "Helena_86.mp3"
    he "Se llama Chancho."
    hide chancho chiqui
    nvl clear
    voice "N476.mp3"
    nvle "Chancho se esconde ligeramente detrás de Helena, pero no deja de mirar al hombre."
    show bg contacto interior
    show contacto mano at right
    $ mama = True
    $ chancho = True
    $ dijo = True
    $ contacto_contador = 0

    label contacto:
        ##### Decision
        show contacto mano at right

        voice "Contacto_04.mp3" 
        menu:
            nvle "¿Qué quieren saber?"
            "¿Sabes qué le pasó a mi mamá?" if mama:
                voice "Helena_87.mp3"
                he "¿Sabes qué le pasó a mi mamá?"
                
                voice "Contacto_05.mp3" 
                co "Es difícil de explicar."
                $ contacto_contador = contacto_contador +1
                $ mama = False
                jump contacto

            "¿Qué sabes de Chancho?" if chancho:
                voice "Helena_88.mp3"
                he "¿Qué sabes de Chancho?"
                voice "Contacto_06.mp3" 
                co "Un sujeto en observación. Ni siquiera cómo llegó a ser lo que es. Pero tu madre... lo protegió."
                
                he "¿Crees que aún lo estén buscando?"
                voice "Contacto_07.mp3" 
                co "Es probable."
                $ contacto_contador = contacto_contador +1 
                $ chancho = False
                jump contacto

            "¿Mi madre te dijo algo antes de desaparecer?" if dijo:
                he "¿Mi madre te dijo algo antes de desaparecer?"
                voice "Contacto_08.mp3" 
                co "Hortensia me contactó poco antes de desaparecer."
                co "Dijo que había encontrado algo… Lo escondió. Me pidió ayuda para mantenerlo seguro."
                voice "Contacto_8.mp3" 
                co "Le debía algunos favores. Así que acepté sin hacer preguntas. Ella me agradeció, como siempre. Dijo que volvería pronto… Pero, bueno... no volvió."
                $ contacto_contador = contacto_contador +1
                $ dijo = False
                jump contacto

            
            "Ya es todo." if contacto_contador >2 :

                ""

    voice "N478.mp3"
    nvle "El contacto camina hacia una estantería y saca un sobre maltratado y sucio, con cinta adhesiva en los bordes. Se lo tiende a Adara, quien lo toma con cautela."
    show contacto sobre at right
    
    voice "Helena_92.mp3"
    he "¿Qué es esto?"
    voice "Contacto_11.mp3" 
    co "Algo que logré recuperar después de que las cosas se pusieron feas."
    hide contacto sobre
    voice "N479.mp3"
    nvle "Adara abre el sobre con cuidado. Fotos y papeles arrugados caen sobre la mesa."
    voice "N480.mp3"
    nvle "Entre ellos, destaca una hoja blanca, amarillenta por el tiempo.  {p=1.0} En el center, a máquina: “SUS SCROFA SUJETO EN OBSERVACIÓN” "
    voice "Helena_93.mp3"
    he "¿Ese es su archivo?"
    voice "Contacto_12.mp3" 
    co "Una vez alguien entró aquí. Me revolvieron todo. Pero no se llevaron nada. Parece que no encontraron lo que buscaban."
    voice "N481.mp3"
    nvle "Helena sostiene la hoja con el nombre “SUS SCROFA” con fuerza."
    voice "N482.mp3"

    nvle "Un vehículo oscuro se detiene frente a la casa. No apaga el motor. Sólo permanece ahí, vibrando, dejando que su presencia se anuncie con ese zumbido mecánico constante."
    voice "N483.mp3"
    nvle "El contacto se aproxima a uno de los monitores de vigilancia. Cambia de cámara. Su ceño se frunce."
    voice "Contacto_13.mp3" 
    co "¿Alguien los siguió?"
    voice "Adara_42.mp3"
    ad "No... No que sepamos."
    

    ##### INTERACCIÓN CONTACTO ######################
    #################################################
    voice "N484.mp3"
    nvle "El contacto se congela un segundo para ver el monitor."
    show camarablur
    voice "N485.mp3"
    nvle "Ajusta el enfoque de la cámara"
    play sound "audio/Foley/Camera Zoom.mp3"
    $ slider_SM = SpriteManager(update=slider_update)
    $ slider_sprites = []


    # Slider variables
    $ slider_bar_size = (545, 70)
    $ slider_image = Image("slider.png")
    $ slider_transform = Transform(child=slider_image, zoom=0.5)
    $ slider_sprites.append(slider_SM.create(slider_transform))
    $ slider_sprites[-1].type = "slider"
    $ slider_sprites[-1].direction = "left"
    $ slider_size = (48, 100)
    $ slider_speed = 6
    $ stop_slider = False

    # Safe zone variables
    $ safe_zone_size = (149, 70)
    $ safe_zone_image = Image("safe-zone.png")
    $ safe_zone_transform = Transform(child=safe_zone_image, zoom=0.5)
    $ safe_zone_sprite = slider_SM.create(safe_zone_transform)
    $ safe_zone_sprite.x = (slider_bar_size[0] - safe_zone_size[0]) / 2  # posición centrada
    $ safe_zone_sprite.y = 0
    $ safe_zone_sprite.type = "safe-zone"
    $ slider_sprites.append(safe_zone_sprite)

    # Chest variables
    $ chest_unlocked = False
    $ chest_unlock_tries = 2
    $ chest_difficulty = 1

    show camara atl transitions behind camaraov
    
    call screen drag_cupon_screen

    image camara atl transitions:
        "camarablur" with dissolve
        pause 0.9
        "camara" with dissolve
        pause 0.4
        repeat
    #################################################
    #################################################

    label next:
        scene bg contacto interior
        nvl clear
        voice "Contacto_14.mp3" 
        co "Tienen que irse."

    show contacto_video with dissolve
    play sound "audio/GolpearPuertaContacto.mp3"
    voice "N486.mp3"
    nvle "Chancho se sobresalta y se esconde tras un grupo de cajas oxidadas. Helena se levanta de golpe, alerta."
    voice "Secuaz4.mp3"
    s1 "Sabemos que están ahí."
    voice "Contacto_15.mp3" 
    co "...Ella los envió."
    voice "Helena_94.mp3"
    he "¿Quién?"
    voice "Contacto_16.mp3" 
    co "Elodia Rivas."
    voice "Contacto_17.mp3" 
    co "Ella debió llevarse a tu madre. Investigación clandestina. Oscura. Fracturados. El virus. Vienen por él."
    show chancho sentado at leftdown with dissolve
    voice "N487.mp3"
    nvle "Apunta a Chancho. El niño, aún tras las cajas, aprieta los ojos con fuerza."
    voice "Contacto_18.mp3" 
    co "Elodia no aceptó sus errores e insiste en seguir cometiendolos, ella aparece en los registros, pero todo pasa por ella. Tu madre...se cruzó en su camino. Y cuando eso pasa... no hay vuelta atrás."
    scene bg contacto interior blur with dissolve
    nvl clear
    voice "N488.mp3"
    nvle "El contacto se apresura. Abre un compartimento en el suelo, oculto bajo una lámina y una alfombra rota. "
    voice "Contacto_19.mp3" 
    show contacto caja
    co "Aquí está todo lo que logré juntar. Información, nombres, rutas, fechas. No es mucho... pero será suficiente."
    voice "Contacto_20.mp3" 
    co "¡Por la ventana trasera! ¡Ya!"
    show contacto mano
    voice "N489.mp3"
    nvle "Adara no duda. Corre hacia la parte de atrás. Quita el seguro de una ventana estrecha, empuja el marco que cruje con el esfuerzo, astillado cae al suelo. Chancho se lanza primero ágilmente. Helena lo sigue con la caja metálica contra el pecho."
    play sound "audio/Foley/Ventana rompiendose.mp3"
    voice "Contacto_21.mp3" 
    co "¡No se detengan! ¡No miren hacia atrás!"
    hide contacto mano 
    voice "N490.mp3"
    nvle "Justo cuando Helena atraviesa el marco, alcanza a escuchar cómo la cerradura cede. La puerta principal se abre de golpe."

    scene black with fade3
    nvl clear
    show huida
    voice "N491.mp3"
    nvle "Dentro de la casa, se escucha un golpe sordo. Un ruido seco. Luego, voces. Y después, silencio."
    voice "N492.mp3"
    nvle "Los tres corren por un callejón angosto rodeado de matorrales secos y cercas rotas entre montones de chatarra, basura acumulada y muros carcomidos por la humedad. Helena abraza la caja metálica con fuerza."
    voice "Helena_95.mp3"
    he "¡Rápido! ¡A la izquierda!"

    scene black with dissolve
    nvl clear
    voice "N493.mp3"
    nvle "El sol comienza a esconderse tras las nubes. El aire es espeso, cargado de polvo y tensión. El camino se vuelve de tierra. Comienzan a internarse en el borde de un bosque gris y húmedo."
    

    ###### Bosque y caja ############################
    #################################################
    
    scene bg noche with fade3
    nvl clear
    if persistent.audio_cues:
        $ Descripcion = "Se escucha un arrollo, fauna nocturna"
    play sound "audio/bosqueNoche.mp3"

    voice "N494.mp3"
    nvle "Ya no se oye a nadie detrás de ellos, pero ninguno se detiene todavía." with dissolve
    voice "N495.mp3"
    nvle "Chancho respira con dificultad. Helena se detiene por fin, jadeante, con la caja metálica apretada contra su pecho."
    voice "N496.mp3"
    nvle "Se han adentrado en el bosque. Adara se seca el sudor con la manga. Helena camina en círculos breves, perdida en su propio cuerpo."
    show i_he_deterioro at leftdialogue with easeinleft
    voice "Helena_96.mp3"
    he "¿Nos siguen?"
    voice "N497.mp3"
    nvle "Adara niega con la cabeza, aún sin aliento. Silencio. Solo el murmullo del viento entre los árboles."
    voice "Helena_97.mp3"
    he "No puedo más... Esto va más allá de mí y de mi mamá."
    if persistent.audio_cues:
        $ Descripcion = ""

    show i_ad_deterioro at right with easeinright
    voice "Adara_43.mp3"
    ad "Lo sé, pero ahora estamos en esto."
    nvl clear
    voice "N498.mp3"
    nvle "Helena agacha la cabeza. Sus lágrimas se deslizan sin control por su rostro en silencio. Adara se acerca a Helena y toca su brazo."
    voice "Adara_44.mp3"
    ad "Lena... no tienes por qué seguir si no quieres."

    play sound "audio/fogata.mp3"
    voice "Helena_98.mp3"
    he "No tengo idea de qué está pasando. No sé si quiero saber. No sé si... quiero seguir."
    voice "Adara_45.mp3"
    ad "Nadie te obliga a seguir buscando, pero admito que no serías tú si no lo haces."
    voice "Helena_99.mp3"
    he "¿Y tú qué harías?"
    scene bg helena adara with fade3
    nvl clear
    voice "Adara_46.mp3"
    ad "Yo... Me iría contigo, a cualquier parte."

    scene bg noche with dissolve
    nvl clear

    ###### INVESTIGO Decision #######################
    menu: 
        
        "¿Y si solo… seguimos adelante sin mirar atrás?(adara)" if novias_flag: #RUTA ADARA    
            $ principal_flag = False
            
            show i_he_tres at leftdialogue with easeinleft
            voice "Helena_101.mp3"
            he "¿Y si solo... seguimos adelante sin mirar atrás?"
            show i_ad_tres at right with easeinright
            voice "Adara_47.mp3"
            ad "Acepto"
            nvl clear
            
        
        "¿Y si solo… seguimos adelante sin mirar atrás?" if principal_flag: #RUTA SECUESTRO
            $ principal_flag = False  #Me sali de la ruta principal 
            $ secuestro_flag = True #Entro a la ruta secuestro
            show i_he_tres at leftdialogue with easeinleft
            voice "Helena_101.mp3"
            he "¿Y si solo... seguimos adelante sin mirar atrás?"
            nvl clear

        "Debo seguir investigando.":
            $ novias_flag = False
            show i_he_tres at leftdialogue with easeinleft
            voice "Helena_102.mp3"
            he "Debo seguir investigando."
            nvl clear
    ##### INVESTIGO

    scene bg noche
    nvl clear
    voice "N498.mp3"
    nvle "Helena vuelve la mirada a Chancho. Él la observa sin juicio. Inocente. Humano y no."
    
    voice "Helena_103.mp3"
    show chancho at center with dissolve
    he "¿Y si lo dejamos aquí?"
    show i_ad_tres at right with dissolve
    voice "Adara_48.mp3"
    ad "Hay que quedarnoslo."

    show fogata with fade3
    if persistent.audio_cues:
        $ Descripcion = "Se escucha el arder del fuego"

    voice "N500.mp3"
    nvle "Se han detenido junto a unas piedras cubiertas de musgo improvisando un campamento entre raíces y piedras.. Adara enciende una pequeña fogata. Chancho se acurruca contra un tronco."
    voice "N501.mp3"
    nvle "Helena se sienta sobre una piedra húmeda. Apoya la caja metálica en sus rodillas. La observa como si pesara una tonelada. No la abre. Solo la mira."
    voice "N502.mp3"
    nvle "Y entonces, rompe en llanto."

    if persistent.audio_cues:
        $ Descripcion = ""
    
    show helena decadencia at leftdown with dissolve
    voice "N503.mp3"
    nvle "No un llanto de pánico. No uno histérico, sino uno lento, contenido. De agotamiento. De duelo. De estar perdiéndose. Chancho se le acerca. No dice nada."
    show chancho at right with dissolve
    voice "N504.mp3"
    nvle "Chancho saca de su bolsillo una flor aplastada, una caléndula medio deshecha, embarrada y se la ofrece. Es un gesto torpe, infantil, pero sincero."
    voice "N505.mp3"
    nvle "Helena la toma con manos temblorosas."
    
        
    if novias_flag:
        jump novias #jump porque no vuelvo

    if secuestro_flag:
        jump secuestro #jump porque no vuelvo

    hide helena decadencia
    show i_he_tres at leftdialogue
    voice "Helena_104.mp3"
    he "Lo único que tengo claro... es que si la encuentro, quiero que esté viva. Y si no... quiero saber por qué."
    show i_ad_tres at right 
    voice "Adara_49.mp3"
    ad "Entonces eso haremos. Buscar respuestas. Aunque duelan."
    
    hide i_ad_tres
    hide i_he_tres
    voice "N506.mp3"
    nvle "Por ahora, han decidido seguir, pero la duda sobre su madre, sobre Chancho, sobre sí misma, se ha vuelto una semilla viva en su interior. Y está creciendo."
    
    
    ###### Principal  ###############################
    #################################################
    $ ui_sueño = True
    label bosqueUI_label:
        $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)
        hide screen arbol_screen
        $ principal_flag = True
        $ novias_flag = False
        $ coqueteo_flag = False
        $ flash_flag = False
        $ secuestro_flag = False
        $ salvar_flag = False
        $ caminoa_flag = False
        $ caminob_flag = False

    scene bg noche with fade3
    nvl clear
    voice "N507.mp3"
    nvle "Una pequeña fogata se ha extinguido hace rato."
    voice "N508.mp3"
    nvle "Adara duerme recostada cerca de la fogata. Chancho reposa hecho bolita a sus pies. Helena se ha sentado cerca, con la caja metálica entre las piernas. La mira en silencio."
    
    scene black with fade3
    nvl clear
    voice "N509.mp3"
    nvle "El sueño llega sin permiso."

    ###### Sueño  ###################################
    #################################################
    scene bg carnes with fade1
    play sound "audio/Ambientacion/IN 1.mp3"
    nvl clear
    voice "Hugo4.mp3"
    hu "Sé una buena niña... solo un bocado más."

    #TRACK 5 Sueño
    play sound "track 5 Sueno Final.mp3"

    scene bg plato
    nvl clear
    play sound "audio/Foley/Corazón latiente.mp3"
    voice "Nina_22.mp3" 
    he "¿Dónde estás?"
    play sound "audio/Ambientacion/IN 1.mp3"
    ################################################

    scene bg bosque dia with fade1
    nvl clear
    voice "N510.mp3"
    nvle "Helena se despierta de golpe. Jadea, se lleva una mano a la boca. Está cubierta de sudor."
    voice "N511.mp3"
    nvle "Adara se ha despertado también. La observa, sin decir nada. Solo se acerca. Se sienta a su lado, en silencio. Helena apoya la cabeza en su hombro. Adara no la aparta."

    show i_ad_tres at right with easeinright
    voice "Adara_50.mp3"
    ad "¿Fue muy feo?"
    voice "N512.mp3"
    nvle "Helena asiente con un leve movimiento."
    show i_he_tres at leftdialogue with easeinleft
    voice "Helena_106.mp3"
    he "No la encontraba. Comía y comía... pero ella no estaba."
    voice "Adara_51.mp3"
    ad "No estás sola, ¿sí? Aunque parezca que todo se rompe... no estás sola."
    voice "N513.mp3"
    nvle "Helena no responde. Solo cierra los ojos un instante."

    scene bg calle
    nvl clear
    voice "N514.mp3"
    nvle "Helena, Adara y Chancho se acercan a la casa de Helena. La puerta está cerrada. Pero el marco está astillado."
    show bg casa dos

    show i_ad_frente at right with easeinright
    voice "Adara_52.mp3"
    ad "¿Siempre estuvo así?"
    show i_he_lateral at left with easeinleft
    voice "Helena_107.mp3"
    he "No..."
    voice "N515.mp3"
    nvle "Chancho se queda en la entrada, inquieto. Mira con temor cada rincón."
    voice "Helena_108.mp3"
    show chancho sentado at center
    he "Vinieron a buscar ese algo."
    voice "N516.mp3"
    nvle "Adara asiente. No dice nada. Las ventanas están cerradas y aún así el ambiente se mantiene helado."
    voice "Adara_53.mp3"
    ad "¿Será buena idea quedarnos?"

    ##### Decision
    menu: 
        "Sí, dudo que vuelvan.":
            voice "Helena_109.mp3"
            he "Sí, dudo que vuelvan."
            voice "Adara_54.mp3"
            ad "Tienes razón."

        "¿Vamos a tu casa?":
            voice "Helena_110.mp3"
            he "¿Vamos a tu casa?"
            voice "Adara_55.mp3"
            ad "Tal vez fueron para allá."

   
    hide i_he_lateral 
    show i_he_tres at leftdialogue
    voice "Helena_112.mp3"
    he "Entonces creo que sí, es seguro dormir aquí."
    
    scene bg casa dos
    nvl clear
    voice "N517.mp3"
    nvle "Adara duerme en el sofá. Chancho se ha dormido sobre sus piernas. Helena permanece despierta, en la oscuridad. "


    ###### Caja #####################################
    #################################################
    
    scene bg casa dos with fade1
    nvl clear
    voice "N518.mp3"
    nvle "Observa la caja metálica sobre la mesa. Sus ojos se han quedado abiertos, toda la noche."
    
    scene bg caja abierta with fade3
    nvl clear
    voice "N519.mp3"
    nvle "Adara está sentada en el sofá. Helena, se sienta a la mesa. Frente a ella, la caja, la abre lentamente."
    voice "N520.mp3"
    nvle " Dentro encuentra papeles arrugados, fotografías borrosas, hay una pequeña pistola envuelta en tela negra, un mapa del pueblo dibujado a mano, y en especial hay una foto granulada de una mujer apenas visible."
    voice "N521.mp3"
    nvle "Helena sostiene un momento el bulto con tela negra para mostrar lo que oculta."
    voice "Adara_56.mp3"
    ad "¿Eso es...?"
    voice "Helena_113.mp3"
    he "Sí. Nos dejó un arma."
    voice "N522.mp3"
    nvle "Helena regresa con cuidado la pistola en la caja y saca el mapa. Lo desdobla y observa detenidamente, hay tres X rojas marcadas en el mapa."
    voice "Adara_57.mp3"
    #mapa
    ad "Si seguimos con esto... llegaremos directo hacia ella."
    scene bg casa dos with fade3
    nvl clear
    voice "N523.mp3"
    nvle "Helena guarda silencio. Mira de nuevo la fotografía de su madre, ahora puesta en la pared."

    show i_he_tres at leftdialogue with dissolve
    ##### Decision
    menu: 
        "Ya no hay vuelta atrás.":
            voice "Helena_115.mp3"
            he "Ya no hay vuelta atrás."

        "¿Segura que quieres acompañarme?":
            voice "Helena_114.mp3"
            he "¿Segura que quieres acompañarme?"
            show i_ad_tres at right with dissolve
            voice "Adara_58.mp3"
            ad "Sí, vayamos los tres."


    ###### X Fabrica ################################
    #################################################
    scene bg granja interior with fade3
    nvl clear
    voice "N524.mp3"
    nvle "Adara, Helena y Chancho llegan a la primera X marcada en el mapa, ven una fábrica abandonada."
    show i_ad_tres at rightdialogue with easeinright
    voice "Adara_59.mp3"
    ad "¿Estás segura de esto? No sabemos que hay aquí."
    show i_he_tres at leftdown with easeinleft
    ##### Decision
    menu: 
        "No. Pero si Elodia está involucrada...":
            voice "Helena_116.mp3"
            he "No. Pero si Elodia está involucrada en lo de mi mamá tenemos que averiguarlo."

        "No. Pero no puedo quedarme sin buscar la verdad.":
            voice "Helena_117.mp3"
            he "No. Pero no puedo quedarme sin buscar la verdad."

    voice "N525.mp3"
    nvle "Salen de entre las ramas y se dan cuenta de que la única cámara del recinto fue vandalizada y la cerradura del portón está rota. Chancho se acerca a la rejilla oxidada. Adara empuja la reja y abre paso al interior de la fábrica."
    voice "N526.mp3"
    nvle "Helena ve como Chancho se pierde entre los anaqueles de metal. Por otro lado, Adara y Helena caminan con cuidado por el lugar creando un eco de sus pisadas."
    ch "¡OOOOOINK!"
    ch "Oink oink oiink."
    voice "N527.mp3"
    nvle "Chancho sale por debajo de  un anaquel de metal viejo lleno de polvo y telarañas, jala a Helena de su ropa y le apunta el lugar por donde salió."
    voice "Helena_118.mp3"
    he "Okay, ya entendí Chancho. Adara, me ayudas a-."
    voice "N528.mp3"
    nvle "El anaquel es deslizado lentamente revelando una pequeña puerta rota de madera estilo entrada de búnker. Chancho se apresura a meterse de nuevo. Helena tose por todo el polvo que se ha levantado."
    voice "Adara_60.mp3"
    ad "De nada. Vamos, no te quedes atrás."
    
    scene bg laboratorio fabrica with fade3
    nvl clear
    voice "N529.mp3"
    nvle "Ambas bajan por unas escaleras de concreto. Al llegar al final de los escalones, ven que el lugar es mucho más grande de lo que aparentaba."
    ch "Oink oink."
    show i_he_espalda at leftdialogue with easeinleft
    voice "Helena_119.mp3"
    he "Por Dios, ¿qué es este lugar...?"
    show i_ad_frente at right with easeinright
    voice "Adara_61.mp3"
    ad "Parece un laboratorio... O algo peor."
    voice "N530.mp3"
    nvle "Se adentran los tres a explorar. En medio de la sala hay una gran mesa con notas sueltas."
    voice "N531.mp3"
    nvle "Adara toma uno de los papeles. “El virus MA no reacciona igual en todos los organismos. Casos raros muestran mutación espontánea sin intervención externa."
    voice "N532.mp3"
    nvle "Levanta una hoja de libreta, parecen las notas de alguien. ''¿Conciencia preservada? Riesgo de anomalías. Inestabilidad emocional o sentido de identidad alterado.''"
    
    voice "N533.mp3"
    nvle "Abren la puerta de la sala con un símbolo de riesgo biológico, Helena y Adara entran a revisar, pero Chancho chilla y se queda agarrado al marco de la puerta y tiembla ligeramente. Las chicas se voltean a ver un poco preocupadas."
    show chancho at center behind i_ad_frente
    voice "Adara_62.mp3"
    ad "Tranquilo Chancho, nos echas aguas si ves venir a alguien."
    ch "¡OINK!"
    
    scene black with dissolve
    nvl clear
    voice "N534.mp3"
    nvle "Adara encuentra un interruptor para prender la luz, y comienza a reproducirse en una pantalla vieja un video."
    scene bg laboratorio
    nvl clear
    show elodia at center
    voice "Helodia_01.mp3"
    el "La mutación espontánea es el verdadero avance. Si logramos rastrear un sujeto con conciencia preservada, podríamos probar que la evolución no depende del control. Solo de la exposición correcta."
    scene bg pizarron 
    nvl clear
    voice "N535.mp3"
    nvle "De fondo hay un pizarrón con las palabras ''Prototipo Sus Scrofa'' subrayadas, y un poco más lejos se alcanzan a ver fotos Chancho."
    voice "Adara_63.mp3"
    ad "¿Chancho...?"
    voice "Helena_120.mp3"
    he "Ella lo estaba vigilando."
    voice "N536.mp3"
    nvle "Voltean a la entrada para ver cómo se encuentra Chancho y se sorprenden al ver a Chancho hasta el fondo de la habitación." 
    voice "N537.mp3"
    nvle "Ambas chicas lo siguen de cerca hasta llegar a una camilla. Sobre esta ven que hay una mochila con unos tenis blancos."
    voice "Helena_121.mp3"
    he "Estas cosas... son de mi mamá."
    voice "N538.mp3"
    nvle "Un sonido metálico retumba por el pasillo, se mantienen en silencio hasta que una alarma empieza a sonar con luces parpadeantes."
    voice "Adara_64.mp3"
    ad "Tenemos que irnos. Ya."
    voice "Helena_123.mp3"
    he "No nos vamos sin las pruebas."
    voice "N539.mp3"
    nvle "Helena toma rápidamente la carpetas y una memoria USB. Corren y se esconden en una habitación dentro de la sala justo a la par de que entran dos hombres armados."

    scene bg laboratorio
    nvl clear
    show secuaz jaguar at right with moveinright
    voice "Sec3.mp3"
    s1 "Elodia dijo que esto debía quedar limpio."
    
    show secuaz tlacuache at left with moveinleft
    voice "Secuaz5.mp3"
    s2 "Creo que entró alguien."
    voice "Sec2.mp3"
    s1 "Entonces no saldrá."

    scene pistola
    nvl clear
    voice "N540.mp3"
    nvle "Helena al escucharlos desenvaina la pistola. Adara se da cuenta y niega con la cabeza mientras le sostiene el brazo a Helena firmemente."
    voice "Adara_65.mp3"
    ad "Olvídate de ellos, conozco un lugar cerca y creo saber por dónde salir sin que nos vean."
    voice "N541.mp3"
    nvl clear
    nvle "Helena suspira con pesadez y guarda la pistola, Adara la suelta y deciden buscar la salida."


    ###### Maíz Caseta ##############################
    #################################################
    $ ui_fabrica = True
    label casetaUI_label:
        $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)
        hide screen arbol_screen
        $ principal_flag = True
        $ novias_flag = False
        $ coqueteo_flag = False
        $ flash_flag = False
        $ secuestro_flag = False
        $ salvar_flag = False
        $ caminoa_flag = False
        $ caminob_flag = False
        
    scene bg bosque dia with fade1
    nvl clear
    voice "N542.mp3"
    nvle "Helena, Adara y Chancho emergen del túnel oculto, jadeantes, cubiertos de polvo hacía un campo de maíz. Los tres caminan entre las plantas quebradas, sin hablar. El cielo se oscurece con rapidez."
    show i_he_decadencia at leftdialogue
    show i_ad_frente at right
    voice "Helena_124.mp3"
    he "No podemos quedarnos a campo abierto."
    voice "Adara_66.mp3"
    ad "Conozco un lugar. Está cerca."

    scene bg caseta with fade1
    nvl clear
    voice "Adara_67.mp3"
    ad "Hace años trabajé haciendo cableado por esta zona. Nos pagaban por horas, así que encontré un rincón donde podía dormir sin que me vieran. Nunca le dije a nadie. Ni siquiera a tu mamá."
    voice "N543.mp3"
    nvle "Se detienen frente a una caseta de mantenimiento, junto a una torre eléctrica caída. Forzada y anónima, como todo lo que rodea."
    voice "Adara_68.mp3"
    ad "Si no la han saqueado, sigue siendo el lugar más seguro del mundo."
    voice "N544.mp3"
    nvl clear
    nvle "Helena enciende una linterna. Hay una laptop sobre un escritorio."
    scene bg laptop with fade3
    nvl clear
    voice "N545.mp3"
    nvl clear
    nvle "Prende la laptop, la pantalla parpadea. El ventilador zumba como si despertara de un coma."
    
    ##### Input EXP_SAFJA
    label inputt_label:
        $ userr_input = renpy.input("Clave:")
        if userr_input == correct_clave:
            "Correcto"

        else:
            "Incorrecto"
            jump inputt_label

    scene bg usb
    nvl clear
    voice "N546.mp3"
    nvle "Introduce la USB con fuerza. Adara se sienta junto a Helena."
    scene  bg laptop carpetas
    nvl clear

    voice "Adara_69.mp3"
    ad "Un poco muy sospechoso ¿no?"

    play sound "Helodia_02.mp3"
    el "La evolución no puede detenerse. Tampoco se fuerza. Solo se revela... en sujetos con potencial inusual."
    el "Hay quienes tienen la capacidad de percibir lo que otros ni siquiera pueden nombrar. Una médium. Una anomalía preciosa. Si sigue viva... será la clave."
    
    scene bg laptop
    nvl clear
    ##### Decision
    menu: 
        "¿Una médium...?":
            voice "Helena_125.mp3"
            he "¿Una médium...?"

        "Está hablando de mi...":
            voice "Helena_126.mp3"
            he "Está hablando de mi..."
  
    voice "Adara_70.mp3"
    ad "Ella te está buscando. ¿Cómo te conoce?"
    voice "Helena_127.mp3"
    he "Supongo que la sacerdotisa fue más popular de lo que pensaba."

    show i_ad_tres at right with dissolve
    voice "Adara_71.mp3"
    
    show i_he_tres at leftdialogue with dissolve
    voice "Helena_128.mp3"
    he "Primero buscó a Chancho. Encontró a mi mamá. Ahora a mí."
    voice "Adara_72.mp3"
    ad "No van a atraparnos. Ni a él... ni a ti. No si estamos juntas."
    voice "Helena_129.mp3"
    he "¿Por qué quieres estar conmigo? No tienes que ir si no quieres."
    voice "Adara_73.mp3"
    ad "Ay Lena, no es nada, cómo voy a dejar que hagas esto sola."
    
    if coqueteo_flag:
        ###### Coqueteo #################################
        voice "Adara_74.mp3"
        ad "Te quiero."
        voice "Helena_130.mp3"
        he "Yo a ti."

    voice "N547.mp3"
    nvl clear
    nvle "Adara continua navegando entre carpetas."

    voice "Helena_131.mp3"
    he "Son los mismos símbolos. Están en el mapa original. Todos son sitios de Elodia..."
    voice "Adara_75.mp3"
    ad "¿Neutralizados?"
    voice "Helena_132.mp3"
    he "Él no va a ser uno más en esa lista."
    voice "N548.mp3"
    nvl clear
    nvle "Helena toma el mapa y lo compara con el mapa en la laptop."
    voice "Helena_134.mp3"
    he "Mamá... Ella dejó esto. Tiene que ser eso. No es casualidad."
    voice "Adara_76.mp3"
    ad "¿Segura Lena? ¿No será una trampa?"
    voice "N549.mp3"
    nvl clear
    nvle "Helena observa la laptop. Luego a Chancho. Luego a Adara."
    voice "Helena_135.mp3"
    he "Tenemos que enfrentarla. Seguro que no se lo espera."


    ###### XX Granja ################################
    #################################################
    $ ui_laboratorio = True
    label FinalUI_label:
        $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)
        hide screen arbol_screen
        $ principal_flag = True
        $ novias_flag = False
        $ coqueteo_flag = False
        $ flash_flag = False
        $ secuestro_flag = False
        $ salvar_flag = False
        $ caminoa_flag = False
        $ caminob_flag = False
        

    show granja puerta with fade2
    nvl clear
    voice "N550.mp3"
    nvle "Un lugar olvidado entre árboles torcidos y maleza sin pisar. La granja está podrida de tiempo, pero aún en pie. Los alambres oxidados crujen con el viento. Chancho olfatea entre hojas secas y tablones flojos."
    
    ""
    scene bg granja interior with dissolve
    nvl clear
    ""

    scene bg mama
    nvl clear
    voice "N551.mp3"
    nvle "En una sala lateral, encuentran una pared de monitores. Uno de ellos muestra una figura encorvada y de espaldas, cubierta por una manta."
    show i_he_decadencia at leftdown
    
    voice "Helena_136.mp3"
    he "Esa blusa... es de mi mamá."
    show i_ad_tres at right
    voice "Adara_77.mp3"
    ad "¡Está viva!"


    ###### Laboratorio ################################
    #################################################
    scene bg mama
    nvl clear
    voice "N552.mp3"
    nvle "Un leve ruido. {p=1.5} La puerta se abre lentamente y Elodia Rivas aparece. Vestida con una bata blanca, guantes quirúrgicos, botas limpias. Su rostro no muestra sorpresa."
    show i_el_frente  at center
    voice "Helodia_03.mp3"
    el "Me alegra conocerte por fin, Helena."
    show i_he_espalda at leftdialogue
    hide i_el_frente
    show i_el_tres at right with easeinright
    #show i_ad_frente at right

    ##### Decision
    menu: 
        "¿Eres tú? ¿La que nos vigilaba?":
            voice "Helena_137.mp3"
            he "¿Eres tú? ¿La que nos vigilaba?"

        "¿Elodia?":
            voice "Helena_138.mp3"
            he "¿Elodia?"

    hide i_he_espalda with dissolve
    voice "Helodia_04.mp3"
    el "Tu madre no entendía lo que protegía. Todo fue observación. Precaución. Pero tú... Tu vínculo con la carne, con la memoria... es extraordinario."
    show chancho sentado at left
    voice "N553.mp3"
    nvl clear
    nvle "Chancho se adelanta, protegiendolas. Elodia lo observa como si viera un milagro."
    el "Y tú... Un espontáneo. Libre. Un resultado que ni el virus pudo predecir."
    show i_ad_frente at left with easeinleft
    voice "Adara_78.mp3"
    ad "¿Dónde está Hortensia?"
    voice "Helodia_05.mp3"
    el " Donde siempre ha estado. En medio de lo que no comprendemos. Su cuerpo resistió el virus. Pero no del todo. Quiso luchar. Pagó el precio."
    hide i_ad_frente
    hide i_el_tres
    show i_he_espalda at center with easeinright
    voice "Helena_139.mp3"
    he "Llévame con ella."
    
    scene black with fade1
    nvl clear
    voice "N554.mp3"
    nvle "Elodia duda un momento. Luego, asiente con un gesto seco."

    show mamaCatre
    voice "N555.mp3"
    nvl clear
    nvle "Hortensia se levanta, pero algo en su cuerpo se tuerce. Sus movimientos son antinaturales. Fragmentada."
    voice "mama8.mp3"
    ho "Hija... Vete..."
    voice "N556.mp3"
    nvl clear
    nvle "Helena da un paso adelante. Llora, pero no grita. Está en shock."
    voice "Helena_140.mp3"
    he "Mamá..."
    
    show elodia tres at right with easeinright
    voice "Helodia_06.mp3"
    el "Ella no es completamente una fracturada. Pero tampoco humana. No puedes curarla."
    voice "Helena_141.mp3"
    show helena lateral at leftdialogue with easeinleft
    he "Tú hiciste esto."
    voice "Helodia_07.mp3"
    el "No. El mundo la hizo así. Yo solo quise entenderlo...antes de que fuera irreversible."
    hide elodia tres
    voice "N557.mp3"
    nvl clear
    nvle "Hortensia avanza. No con furia. Con dolor. Con peso. Como si sus propios huesos se arrastraran por dentro."
    

    ###### ¿MATO a mi madre? ################################
    #################################################
    voice "Helena_142.mp3"
    he "Mamá estás sufriendo."
    
    ###### MATO Decision ############################
    menu: 
        "¿Mato a mi mamá?"
        "Lo siento... mamá":
            ###### Matamos a la mamá #####
            scene bg apunta mama with fade2
            nvl clear
            voice "Helena_143.mp3"
            he "Lo siento... mamá"
            voice "Adara_79.mp3"
            ad "¡Helena, no!"

            if persistent.audio_cues:
                $ Descripcion = "Disparo"

            $ renpy.movie_cutscene("disparo_mama.ogv", stop_music=True)
            show bg mama with fade1
            show hortensia muerta
            voice "N558.mp3"
            nvle "Dispara. Hortensia cae. No como monstruo. {p=1.5} Sino como un cuerpo inerte."

            if persistent.audio_cues:
                $ Descripcion = ""
            
        "No puedo":
            ###### Salvamos a la mamá #####
            scene bg apunta mama
            nvl clear
            voice "Helena_42.mp3"
            he "No puedo"
            ""
            voice "N559.mp3"
            nvle "Apunta al candado de la celda, se acerca a abrazarla."
            $ salvar_flag = True
    ###### MATO

    scene bg laboratorio
    nvl clear
    voice "N560.mp3"
    nvle "Elodia camina hacia ellas. Despacio. Sin temor."
    voice "Helodia_08.mp3"
    el "Ahora entiendes lo que yo entendí. La conciencia no es inmortal. Pero el recuerdo sí."
    scene pistola
    nvl clear
    voice "N561.mp3"
    nvle "Helena apunta. Tiembla."
    voice "Helodia_09_02.mp3"
    el "No tienes que matarme. Podrías superarme. Heredar el proyecto. Perfeccionarlo."
    voice "Helena_43.mp3"
    he "No quiero ser tú."
    voice "Helodia_010.mp3"
    el "¿Estás segura?"
    voice "N562.mp3"
    nvl clear
    nvle "Helena baja el arma por un segundo... pero solo para tener un ángulo que le permita disparar mejor."
    voice "N563.mp3"
    play sound "audio/Foley/Disparo.mp3"
    nvle "Da un solo disparo. {p=1.5} No cae de inmediato, pero la sangre empieza a brotar lentamente."
    voice "Helodia_11.mp3"
    el "Curioso... Pensé que... ibas a..."
    voice "N564.mp3"
    nvl clear
    nvle "Cae. Sin gloria. Sin redención. {p=1.5} Mientras tanto Chancho se come los cables de refrigeración del sistema."
    

    ###### Se quema #################################
    #################################################
    scene bg laboratorio tubo
    nvl clear
    voice "N565.mp3"
    nvle "Adara y Helena quitan a Chancho, pero los equipos mordidos comienzan a sobrecalentarse y prenden fuego. El lugar se derrumba."
    
    if salvar_flag:
        scene black
        nvl clear
        voice "N566.mp3"
        nvle "Hortensia es alcanzada por las llamas y muere."
        voice "Helena_44.mp3"
        he "¡Mamááááááááá!"
        scene black with fade1
    
    nvl clear
    voice "N567.mp3"
    nvle "La salida colapsa a sus espaldas. Helena y Adara caminan sin mirar atrás."

    if salvar_flag == False:
        scene black with fade1
        nvl clear
        show granja
        voice "Adara_80.mp3"
        ad "¿Por qué lo hiciste?"
        voice "Helena_45.mp3"
        he "Eso ya no era mi mamá."

    if salvar_flag:
        scene black
        nvl clear
        show granja with fade1
        voice "Adara_81.mp3"
        ad "Ni siquiera pienses que fue tu culpa, Lena."
        voice "Helena_46.mp3"
        he "Gracias, Ara. Por eso mi mamá te quería tanto."
        voice "Adara_82.mp3"
        ad "¿Nada más tu mamá?"
        voice "Helena_47.mp3"
        he "Bueno, yo también."

    show i_ad_frente at right with easeinright
    voice "Adara_83.mp3"
    ad "¿A dónde iremos?"
    voice "Helena_48.mp3"
    show i_he_tres at leftdialogue with easeinleft
    he "Hasta donde no recordemos lo que hemos pasado."
    scene bg manos
    nvl clear
    voice "N568.mp3"
    nvle "Se toman la mano, en la otra mano de Helena, el mapa. {p=1.5} Tres X. Una tachada. Otra en el puño."
    voice "N569.mp3"
    nvle "La tercera... seguirá esperando."
    

    ###### FINAL 1 ##################################
    #################################################
    # FIN
    $ final_arbol = True
    scene black with fade1
    show screen arbol_screen with fade1
    ""
    ""
    ""
    ""
    return

###################################################################################
###################################################################################

###### Declaración de posiciones
transform controlposition:
    xpos 1280
    ypos 110

transform right:
    xpos 900
    ypos 50

transform rightdown:
    xpos 900
    ypos 500

transform left:
    xpos 0
    ypos 50

transform leftdown:
    xpos 150
    ypos 300

transform leftdialogue:
    xpos 0
    ypos 100

transform rightdialogue:
    xpos 900
    ypos 200

transform chiqui:
    xpos 350
    ypos 650

transform centerleft:
    xpos 500
    ypos 200

transform centerright:
    xpos 900
    ypos 200

transform center:
    xpos 620
    ypos 400

transform centerup:
    xpos 620
    ypos 250

transform rightup:
    xpos 900
    ypos 100

transform righter:
    xpos 1300
    ypos 400

##### Lyrics videos
image song1 = Movie(play="Song1.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080), loop =False)

###### Declaración de videos
image HelenaSuicida = Movie(play="Helenasuicida.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image insolacion = Movie(play="Insolacion.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080), loop =False)
image fogata = Movie(play="fogata.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image carneVelas = Movie(play="velas_y_carne.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image pruebaCarne = Movie(play="PruebaCarnePrimeraVez.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))  
image FB_suicidio = Movie(play="ChicaSuicidx.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))  
image almas = Movie(play="Ojosalmas.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))  
image contacto_video = Movie(play="intContacto_fondo.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))  
image CelularFuneral = Movie(play="celular.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image CelularDos = Movie(play="CelularDos.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image CartaMama = Image("images/CartaMama.png", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image fbtormento = Movie(play="bg_flashback_tormento.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image fbojos = Movie(play="Fb_ojosInicio.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image huida = Movie(play="Huida.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image mamaCatre = Movie(play="hortensiaCorrompida.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image mamaCatrePantalla = Movie(play="PantallaLaboratorio secuestro.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image disparoMama = Movie(play="hortensiaCorrompida.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image lavabo = Movie(play="lavabo.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image Helenasuicida = Movie(play="Helenasuicida.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image ojosChancho = Movie(play="ojosChancho.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image chanchohuye = Movie(play="chanchohuye.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image granja = Movie(play="Granjahumo.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image camasex = Movie(play="Bg_cama2.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image laboratorio_alarma = Movie(play="laboratorio_alarma.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image laboratoriotubo = Movie(play="laboratoriotubo.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image camasex = Movie(play="Bg_cama2.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))
image reloj = Movie(play="reloj.ogv", xpos=0.5, ypos=0.5, xanchor=0.5, yanchor=0.5, size=(1920,1080))

##### Animación
image papas:
    "bg papas uno"
    pause 1.0
    "bg papas dos"
    pause 1.0
    repeat
 
##### Declaración de imagenes
image i_he = At('helena', sprite_highlight('hel'))
image i_he_tres = At('helena tres', sprite_highlight('hel'))
image i_he_tress = At('helena tress', sprite_highlight('hel'))
image i_he_espalda = At('helena espalda', sprite_highlight('hel'))
image i_he_lateral = At('helena lateral', sprite_highlight('hel'))
image i_he_decadencia = At('helena decadencia', sprite_highlight('hel'))
image i_he_deterioro = At('helena deterioro', sprite_highlight('hel'))
image i_he_enojo = At('helena enojo', sprite_highlight('hel'))
image i_he_bgrande = At('helena bata grande', sprite_highlight('hel'))
image i_he_sec = At('helena secuestro', sprite_highlight('hel'))

image i_ad = At('adara', sprite_highlight('ada'))
image i_ad_tres = At('adara tres', sprite_highlight('ada'))
image i_ad_frente = At('adara frente', sprite_highlight('ada'))
image i_ad_enojada = At('adara enojada', sprite_highlight('ada'))
image i_ad_deterioro = At('adara deterioro', sprite_highlight('ada'))

image i_el_tres = At('elodia tres', sprite_highlight('elo'))
image i_el_tress = At('elodia tress', sprite_highlight('elo'))
image i_el_frente = At('elodia frente', sprite_highlight('elo'))


image i_hu = At('hugo', sprite_highlight('hug'))
image i_ho = At('hortenssia', sprite_highlight('hor'))


##### SCREENS para interacciones ##################################################
###################################################################################

##### Interacción Anaquel
label anaquelfake_label:
        nvle "¿Debería buscar algo aquí"

screen anaquel_screen():
    modal True
    image "bg pasillo.png"
    imagebutton:
        idle "anaquelDos_Idle.png"
        hover "anaquelDos_hover.png"
        xpos 94
        ypos 526
        anchor (0.5, 0.5)

        action Function(anaquel_func)

    imagebutton:
        idle "anaquelUno_idle.png"
        hover "anaquelUno_hover.png"
        xpos 1070
        ypos 535
        anchor (0.5, 0.5)

        action Function(anaquelfake_func)
            
screen cupon_screen():
    modal True

    imagebutton:
        idle "maquina_idle.png"
        hover "maquina_hover.png"
        xpos 0.57
        ypos 0.49
        anchor (0.5, 0.5)
        action Function(cupon_func)

screen refri_screen():
    modal True
    image "bg congelador.png"
    imagebutton:
        idle "RefriDerecha_idle.png"
        hover "RefriDerecha_hover.png"
        xpos 0.7753
        ypos 0.528
        anchor (0.5, 0.5)

        action Function(refri_func)

    imagebutton:
        idle "RefriIzquierda_idle.png"
        hover "RefriIzquierda_hover.png"
        xpos 398
        ypos 94
        anchor (0.5, 0.0)

        action Function(refrifake_func)

##### Interacción CUARTO
screen cuarto_screen():
    modal True
    image "bg hortensia.png"
    imagebutton:
        idle "cuarto_cama_idle.png"
        hover "cuarto_cama_hover.png"
        xpos 1920
        ypos 1080
        anchor (1.0, 1.0)

        action Function(cuartofake_func)

    imagebutton:
        idle "cuarto_espejo_idle.png"
        hover "cuarto_espejo_hover.png"
        xpos 1076
        ypos 785
        anchor (1.0, 1.0)

        action Function(cuartofake_func)

    imagebutton:
        idle "cuarto_marco_idle.png"
        hover "cuarto_marco_hover.png"
        xpos 1347
        ypos 384
        anchor (1.0, 1.0)

        action Function(cuartofake_func)

    imagebutton:
        idle "cuarto_pintura_idle.png"
        hover "cuarto_pintura_hover.png"
        xpos 1920
        ypos 0
        anchor (1.0, 0.0)

        action Function(cuartofake_func)

    imagebutton:
        idle "cuarto_closet_idle.png"
        hover "cuarto_closet_hover.png"
        xpos 0
        ypos 574
        anchor (0.0, 0.5)

        action Function(cuartofake_func)

    imagebutton:
        idle "cuarto_buro_idle.png"
        hover "cuarto_buro_hover.png"
        xpos 1395
        ypos 760
        anchor (1.0, 1.0)

        action Function(cuarto_func)

##### Interacción Contacto 
screen drag_cupon_screen:
    key ["K_SPACE", "mousedown_1"] action If(chest_unlocked, [Hide("drag_cupon_screen", transition=Fade(1, 1, 1)), Jump("next")], Function(check_slider_safe_zone))
    image "camaraov.png"
    if not chest_unlocked:
        frame:
            background None
            align (0.5, 0.8)
            xysize slider_bar_size
            image "slider-bar.png" 
            add slider_SM 
        image "chest-closed-idle.png" align (0.5, 0.7) 
    else:
        image "chest-opened.png" #align (0.5, 0.7) 

##### Interacción Cupon
screen drag_sample2:
    draggroup:
        drag:
            drag_name "circle"
            child "cupon.png"
            xpos 20
            ypos 20
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
                
        drag:
            drag_name "The Left Circle"
            xpos 0.4
            ypos 0.5
            child "pos.png"
            draggable False
            droppable True

screen drag_sample3:
    draggroup:
        drag:
            drag_name "The Left Circle"
            xpos 0.5
            ypos 0.6
            child "pos.png"
            draggable False
            droppable False



##### Árbol UI
default ui_nota = False
default ui_adara = False
default ui_chancho = False
default ui_depre = False
default ui_flash = False
default ui_contacto = False
default ui_sueño = False
default ui_secuestro = False
default ui_contexto = False
default ui_esclava = False
default ui_fabrica = False
default ui_laboratorio = False

screen arbol_screen():
    image "bg arbol.png"
    
    image "ui fogata.png":
        xpos 168
        ypos 480

    textbutton "{a=jump:inicioUI_label}Inicio{/a}":
        xpos 164
        ypos 570
        text_size 30

    if ui_adara:
        image "ui adara.png":
            xpos 958
            ypos 124

        textbutton "{a=jump:novias}Adara{/a}":
            xpos 975
            ypos 216
            text_size 30

    if ui_chancho:
        image "ui chancho.png":
            xpos 540
            ypos 835

        textbutton "{a=jump:chancho}Chancho{/a}":
            xpos 537
            ypos 925
            text_size 30    

    if ui_nota:
        image "ui hortensia.png":
            xpos 526
            ypos 423

        textbutton "{a=jump:notaUI_label}Nota{/a}":
            xpos 535
            ypos 513
            text_size 30
    
    if ui_contacto:
        image "ui contacto.png":
            xpos 758
            ypos 342

        textbutton "{a=jump:contactoUI_label}Contacto{/a}":
            xpos 743
            ypos 430
            text_size 30

    if ui_secuestro:
        image "ui secuestro.png":
            xpos 948
            ypos 548

        textbutton "{a=jump:secuestro}Lab{/a}":
            xpos 970
            ypos 642
            text_size 30

    if ui_contexto:
        image "ui contexto.png":
            xpos 1150
            ypos 558

        textbutton "{a=jump:ElodiaUI_label}Elodia{/a}":
            xpos 1150
            ypos 652
            text_size 30

    if ui_esclava:
        image "ui esclava.png":
            xpos 1343
            ypos 558

        textbutton "{a=jump:esclava}Esclava{/a}":
            xpos 1343
            ypos 650
            text_size 30

    if ui_sueño:
        image "ui bosque.png":
            xpos 1015
            ypos 331

        textbutton "{a=jump:bosqueUI_label}Bosque{/a}":
            xpos 1015
            ypos 421
            text_size 30

    if ui_fabrica:
        image "ui caseta.png":
            xpos 1249
            ypos 341

        textbutton "{a=jump:casetaUI_label}X{/a}":
            xpos 1290
            ypos 435
            text_size 30

    if ui_laboratorio:
        image "ui lab.png":
            xpos 1480
            ypos 338

        textbutton "{a=jump:FinalUI_label}Final{/a}":
            xpos 1485
            ypos 434
            text_size 30

    if ui_depre:
        image "ui depre.png":
            xpos 838
            ypos 753

        textbutton "{a=jump:flash}Triste{/a}":
            xpos 838
            ypos 843
            text_size 30

    if ui_flash:
        image "ui flash.png":
            xpos 1020
            ypos 753

        textbutton "{a=jump:FlashUI_label}Recuerdos{/a}":
            xpos 1005
            ypos 848
            text_size 28

    image "bg hilos.png"
        

##### INIT para interacciones ####################################################
##################################################################################
init python:
    ##### Interacción Super
    def anaquel_func():
        renpy.jump("anaquel_label")
        #renpy.hide_screen("anaquel_screen")

    def anaquelfake_func():
        renpy.call("anaquelfake_label")

    def cupon_func():
        renpy.jump("cupon_label")

    def refri_func():
        renpy.jump("refri_label")

    def refrifake_func():
        renpy.jump("refrifake_label")

    def refrifake_func():
        renpy.jump("refrifake_label")

    def cuarto_func():
        renpy.jump("cuarto_label")
        
    def cuartofake_func():
        renpy.jump("cuartofake_label")

    ##### Interacción Maquina
    def drag_placed(drags, drop):
        if not drop:
            return False
        
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        
        return True

    ##### Interacción Contacto
    def slider_update(st):
        global slider_speed

        for sprite in slider_sprites:
            if sprite.type == "slider":
                if round(sprite.x) < slider_bar_size[0] - slider_size[0] and sprite.direction == "right":
                    sprite.x += slider_speed * chest_difficulty
                    slider_speed += 0.04 
                elif round(sprite.x) >= slider_bar_size[0] - slider_size[0] and sprite.direction == "right":
                    sprite.direction = "left"
                    slider_speed = 4
                elif round(sprite.x) > 0 and sprite.direction == "left":
                    sprite.x -= slider_speed * chest_difficulty
                    slider_speed += 0.04
                elif round(sprite.x) <= 1 and sprite.direction == "left":
                    sprite.direction = "right"
                    slider_speed = 4
        if not stop_slider:
            return 0
        else:
            return None

    def check_slider_safe_zone():
        global chest_unlocked
        global chest_unlock_tries
        global stop_slider

        for slider in slider_sprites:
            if slider.type == "slider":
                for safe_zone in slider_sprites:
                    if safe_zone.type == "safe-zone":
                        if safe_zone.x < slider.x < safe_zone.x + safe_zone_size[0]:
                            chest_unlocked = True
                            stop_slider = True
                        elif chest_unlock_tries > 0:
                            chest_unlock_tries -= 1

    def reset_drag_cupon_screen():
        global chest_unlocked
        global chest_unlock_tries
        global stop_slider
        global slider_speed

        chest_unlocked = False
        chest_unlock_tries = 6
        stop_slider = False
        slider_speed = 12

        for sprite in slider_sprites:
            if sprite.type == "slider":
                sprite.x = 0
                sprite.y = 0.7
            elif sprite.type == "safe-zone":
                sprite.x = 100

        slider_SM.redraw(0)
        renpy.restart_interaction()
