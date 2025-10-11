##### RAMAS // AMORDIDAS // AVOCADO STUDIO // EMILIO VELAZQUEZ, FRANCISCO GUZMAN // XIMENA LEON

## FINAL 4 CERDO ####################################
label chancho:
    $ final_arbol = True
    $ ui_chancho = True
    $ config.mouse_displayable = MouseDisplayable("gui/handpointerdos.png", 15, 15)
    hide screen arbol_screen
    $ principal_flag = False
    $ novias_flag = False
    $ coqueteo_flag = False
    $ flash_flag = False
    $ secuestro_flag = False
    $ salvar_flag = False
    $ caminoa_flag = False
    $ caminob_flag = False


    ###### Chancho diferente ########################
    #################################################
    define chancho = "Chancho"
    scene bg cueva with dissolve
    play sound "audio/Ambientacion/IN 1.mp3"
    nvl clear
    voice "N1.mp3"
    nvle "Chancho corre entre el lodo con otros cerdos. Pero él es más alto. Sus patas tiemblan. Sus ojos no son iguales. Los demás cerdos lo miran, y se alejan."
    scene bg chancholodoa with dissolve
    nvl clear
    ch "¿Ya no quieren lodo? Venga, está muy fresco."
    scene bg chancholodob with dissolve
    nvl clear
    voice "N2.mp3"
    nvle "Uno de los cerdos lo empuja. Otro lo ignora. Uno gruñe fuerte, con rechazo. Chancho se aleja, confundido, triste. Cruza un cerco, mira hacia el monte. El cerco no se ve tan alto como antes. Comienza a caminar."
    scene bg cueva with dissolve
    nvl clear
    voice "N3.mp3"
    play sound "audio/Ambientacion/IN 1.mp3"

    nvle "Chancho despierta sobresaltado. Se sacude las hojas con movimientos torpes. Huele el aire. Se calma. Escucha un pájaro. Se emociona. Se pone de pie."
    ch "Flores primero. Luego jugar y esperar a mamá. Siempre así."
    scene bg casa chancho with fade
    nvl clear
    voice "N4.mp3"
    nvle "Chancho se mueve entre las plantas y arbusto, cuidando no hacer ruido. Llega a un jardín. Las plantas están verdes, húmedas."
    voice "N5.mp3"
    nvle "Chancho se acerca a unas en particular: hojas grandes, olor fuerte, dulzón. Unas caléndulas. Las lame. Las mastica despacio."
    voice "N6.mp3"
    nvle "Cierra los ojos. Se acuesta en el pasto, satisfecho. Luego, vuelve a mirar hacia la casa."
    ch "Está, está!? Ya puedo verla."
    voice "N7.mp3"
    nvle "Se acerca a la puerta trasera con pasos cortos. Sube los escalones de madera. Pero se detiene."
    voice "N8.mp3"
    nvle "Chancho se pega a la puerta. Raspa con una pata. Nadie abre. Solo el silencio vuelve. Chancho se acuesta junto a la puerta. La cabeza sobre el piso. Toma una buena sombra y procede a esperar."

    scene bg chancholodo with dissolve
    play sound "audio/Ambientacion/IN 1.mp3"
    nvl clear
    voice "N9.mp3"
    nvle "Chancho, más pequeño, cubierto de lodo. Una figura femenina se acerca. Se agacha. Le deja comida envuelta. Lo observa con ternura."
    voice "mama9.mp3"
    ho "No muerdes, ¿verdad? Yo tampoco."
    nvl clear
    voice "N10.mp3"
    nvle "Le sonríe. Se va. Chancho se queda mirando. No entiende la emoción que le aprieta el pecho."
    play sound "audio/Ambientacion/IN 1.mp3"


    ###### Chancho Helena ###########################
    #################################################
    
    scene bg ventana with fade1
    nvl clear
    voice "N11.mp3"
    nvle "Chancho despierta sobresaltado. Se pone alerta. Se arrastra hasta la ventana lateral. No alcanza a ver muy bien. Algo está mal, pero no sabe que es."
    voice "N12.mp3"
    nvle "Chancho vuelve al jardín. Come otra flor. La mastica con más lentitud. Luego se acuesta."

    voice "N13.mp3"
    nvle "Mira la puerta cerrada y vuelve a acercarse. Esta vez golpea con más insistencia, raspa más fuerte, emite un chillido agudo."
    voice "N14.mp3"
    nvle "La puerta se abre de golpe. Helena con los ojos rojos y el rostro demacrado mira a Chancho."

    scene bg casa_blur with dissolve
    nvl clear
    show helena decadencia at centerup
    voice "he1.mp3"
    he "¿Qué...?"
    voice "he2.mp3"
    he "¡Vete de aquí!"
    voice "N15.mp3"
    nvle "Está por cerrar la puerta. Pero se detiene. Nota en la ropa del cerdito unas motas anaranjadas, restos de caléndula."

    voice "he3.mp3"
    he "¿Tú...?"
    voice "N16.mp3"
    nvl clear
    nvle "Chancho da un paso hacia adentro. Levanta las orejas. Sonríe."

    voice "he4.mp3"
    he "¡No!"
    scene bg mueve maceta with dissolve
    nvl clear
    voice "N17.mp3"
    nvle "Sale de la casa, se dirige al jardín. Toma las macetas intactas. Las mete al interior una a una, colocándolas frente a la ventana. Chancho se acerca a la entrada."
    voice "he5.mp3"
    he "No. Aquí no."
    voice "N18.mp3"
    nvl clear
    nvle "Levanta una escoba y lo ahuyenta. Chancho retrocede unos pasos, confundido, pero no huye. Solo baja la cabeza."

    voice "N19.mp3"
    nvle "Chancho se acurruca frente a la puerta. La noche cae lenta. El frío empieza a aumentar."

    ch "Hoy no salió."
    voice "N20.mp3"
    nvl clear
    nvle "Mira hacia la ventana. Nadie aparece. El cerdito bosteza. Se regresa a su cueva."
    

    ###### Chancho Día 2 ###############################
    #################################################
    scene bg cueva noche with slow_dissolve
    play sound "audio/Ambientacion/IN 1.mp3"
    nvl clear
    voice "N21.mp3"
    nvle "Chancho duerme acurrucado entre hojas."
    
    voice "N22.mp3"
    nvle "Chancho, más joven, más cerdo. Su cuerpo era aún redondo, apenas humano. Su hocico más corto, sus movimientos más torpes. Entre los escombros y lodo de un corral, encuentra un cuerpo humano. No tiene nombre. Solo carne. Chancho lo huele, lo toca, lo prueba."
    
    play sound "audio/Ambientacion/IN 1.mp3"
    voice "N23.mp3"
    nvle "Chancho despierta con sobresalto. Se queda quieto."
    nvl clear
    ch "Hortensia. Hoy sí. Hoy sí viene."
    voice "N24.mp3"
    nvle "Sale de su escondite."

    scene bg ventana with fade
    nvl clear
    voice "N25.mp3"
    nvle "Se acerca a la casa. Se asoma por la ventana, empinándose con dificultad."
    voice "N26.mp3"
    nvle " No hay nadie. {p=1.5} Ve la mesa vacía. La sala revuelta. Pero allí están... las caléndulas. Colocadas en una esquina, dentro."
    nvl clear
    ch "Ella las puso ahí. Para que las viera. Ella está cerca."
    voice "N27.mp3"
    nvle "Chancho se sienta. Mira la ventana. Espera. Las horas pasan. El cielo se pinta naranja."

    voice "N28.mp3"
    nvle "El estómago de Chancho ruge. Se agita. Olfatea con ansiedad. Mira de nuevo la ventana."
    voice "N29.mp3"
    nvle "Chancho se pone de pie. Coloca sus pezuñas sobre el marco."

    voice "N30.mp3"
    nvle "Gira la cabeza. Mete el hocico. {p=1.5} Nada. {p=1.5} Se frustra. Da vueltas. Mira hacia todos lados. Y vuelve a intentarlo."

    voice "N31.mp3"
    nvle "El marco se astilla. La madera vieja cede. Un pequeño hueco. Chancho empuja su cuerpo entre los restos de la ventana."
    play sound "audio/Foley/Ventana rompiendose.mp3"
    if persistent.audio_cues:
        $ Descripcion = "Se escucha una ventana rompiendose"

    ###### Chancho Depresión ###############################
    #################################################
    voice "N32.mp3"
    nvle"Chancho cae dentro con torpeza. Tose. Sacude sus patas. Se arrastra hasta las macetas. Las huele. Las lame. Come con desesperación."
    if persistent.audio_cues:
        $ Descripcion = ""
    voice "N33.mp3"
    nvle "En el fondo... Helena llora en su habitación. No grita. No reacciona al ruido. No sale."
    voice "N34.mp3"
    nvle "Chancho se detiene un momento. Mira en dirección al sonido. Mastica más lento. Luego traga."

    scene bg chanchocomeflor
    nvl clear
    ch "Está llorando otra vez."
    nvl clear
    voice "N35.mp3"
    nvle "Chancho olfatea el aire. La casa huele mal. A sudor seco. A carne vieja."
    voice "N36.mp3"
    nvle "Avanza por el pasillo. {p=1.5} Pasa cerca de una puerta entreabierta. Dentro, todo está limpio. Casi intacto. Un cojín gastado. Un vaso a medio llenar. Una blusa doblada."
    voice "N137.mp3"
    nvle "Chancho se detiene. Huele la puerta. Se queda quieto."
    ch "Aquí... aquí huele a ella."
    nvl clear
    voice "N38.mp3"
    nvle "Chancho entra al cuarto de hortensia, está desordenado, da una vuelta alrededor buscando algo. No lo encuentra y se va."
    ch "Aquí no está"

    scene bg puertahelena with dissolve
    nvl clear
    voice "N39.mp3"
    nvle "Luego sigue avanzando, rumbo al cuarto de Helena."
    voice "N40.mp3"
    nvle "Chancho camina arrastrando las patas, dejando un rastro leve de tierra húmeda. La casa está en penumbra. La puerta del cuarto de Helena está entreabierta. Una tenue luz amarilla se filtra por la rendija. {p=1.5}Se asoma."

    voice "N41.mp3"
    nvle "Helena yace en el suelo."
    voice "N42.mp3"
    nvle "La habitación es un caos. Ropa sucia, papeles arrugados, bandejas vacías, charolas rotas. Una botella volcada chorrea sobre el piso."
    voice "N43.mp3"
    nvle "Chancho entra en silencio. Sus pasos sobre los objetos del suelo suenan como crujidos de hojas secas."

    voice "he6.mp3"
    he "Te dije que no..."
    nvl clear
    voice "N44.mp3"
    nvle "Levanta un poco la cabeza. Lo ve. Reconoce a Chancho. Suspira. Baja la cabeza de nuevo."

    voice "he7.mp3"
    he "Otra vez tú..."
    scene bg chanchotriste with dissolve
    nvl clear
    voice "N45.mp3"
    nvle "Chancho se acerca con cautela. Olfatea su hombro. Ladea la cabeza. Se sienta. La observa."
    voice "N46.mp3"
    nvle "Chancho intenta empujarla con el hocico. Ella no se mueve. Intenta levantar su brazo. Ella lo aparta con una mano temblorosa."

    voice "he8.mp3"
    he "No quiero. Déjame."
    nvl clear
    voice "N47.mp3"
    nvle "Chancho no entiende. Pero siente."

    ch "No está fracturada... sólo... solo que ya no camina."
    nvl clear
    voice "N48.mp3"
    nvle "Helena se voltea, le da la espalda. Chancho retrocede. Sale lentamente del cuarto."


    ###### Chancho solo ###############################
    #################################################
    voice "N49.mp3"
    nvle "Chancho se enrolla en la manta. Tiembla. Cierra los ojos. Trata de dormir"
    voice "N50.mp3"
    nvle "Chancho corre entre ramas. Sus patas están heridas. Su respiración es agitada. Al fondo, luces. Voces humanas. Pasos apresurados."

    scene black
    nvl clear
    show chanchohuye
    voice "Sec1.mp3"
    s1 "¡Ahí va! ¡¡Rápido!!"
    ch "No quiero... no quiero..."
    voice "N51.mp3"
    nvle "Ramas lo arañan. Tropieza. Se arrastra. Se levanta de nuevo. Gira. Está rodeado. Un destello. Una linterna directa a su cara."
    
    voice "Secuaz6.mp3"
    s2 "¡Lo tenemos!"
    hide secuaz tlacuache
    hide secuaz coyote
    voice "N52.mp3"
    nvle "Chancho busca por donde correr. Solloza."
    voice "mama9.mp3"
    ho "¡Ven sube!"
    scene bg hortensiabrazos with dissolve
    nvl clear
    voice "N53.mp3"
    nvle "Chancho la ve. Ella extiende los brazos desde la cabina de una camioneta. Su silueta contra la luz. Se lanza hacia ella. Sube. Ella lo sujeta. Cierra la puerta."
    voice "N54.mp3"
    nvle "Chancho en el asiento trasero. Hortensia le pasa una manta."
    voice "mama10.mp3"
    ho "Shhh... Ya pasó. Ya estás conmigo."
    nvl clear
    voice "N55.mp3"
    nvle "Chancho cierra los ojos. Se acurruca. Sonríe."
    scene bg cueva noche with dissolve
    nvl clear
    voice "N56.mp3"
    nvle "Chancho se despierta. Mira a su alrededor. Sigue solo. El viento sacude las ramas. Su hocico se mueve. Olfatea. Se pone de pie lentamente."
    voice "N57.mp3"
    nvle "De pronto, se detiene. Su hocico se alza. Olfatea. Gira hacia la izquierda. Camina en esa dirección."


    ###### Chancho tumba ###############################
    #################################################
    scene bg funeral hoyo with slow_dissolve
    nvl clear
    voice "N58.mp3"
    play sound "audio/Foley/Pala.mp3"
    if persistent.audio_cues:
        $ Descripcion = "Se escucha la fuerza con la que Helena entierra la pala"
    nvle "Helena, cubierta de barro, cavando. {p=1.5} Está junto a la tumba simbólica donde dejó el código QR de su madre. La tierra ya no es tan blanda. Cada palada parece más pesada que la anterior."
    show chancho parado at center 
    if persistent.audio_cues:
        $ Descripcion = ""
    voice "N59.mp3"
    nvle "Chancho se detiene a unos metros. La observa en silencio. Helena lo ve. No dice nada. No lo echa. Solo lo ve. Sus ojos están llenos, pero secos."
    voice "N60.mp3"
    nvle "Chancho se sienta. {p=1.5} El viento se lleva el silencio."

    voice "N61.mp3"
    nvle "Chancho sigue sentado. Helena ya no cava. Solo se queda junto al agujero, arrodillada, con la pala sobre las piernas."
    voice "N62.mp3"
    nvle "Chancho se pone de pie. Mira hacia el origen del ruido. La casa de Helena. Tensos segundos."
    voice "N63.mp3"
    nvle "Voltea hacia Helena. Ella no reacciona. Mira la tierra. Cierra los ojos. Los sonidos se desvanecen."
    ch "Quizás si no lo ve, no existe."
    nvl clear
    voice "N64.mp3"
    nvle "Chancho y Helena caminan juntos, pero no lado a lado. Hay una distancia entre ellos. Helena camina como si cargara el monte sobre sus hombros. Chancho solo la sigue."
    voice "N65.mp3"
    nvle "Al llegar, Helena se detiene en seco."
    voice "N66.mp3"
    nvle "La puerta está colgando de una sola bisagra. Cristales rotos por todo el jardín. Las plantas volteadas. Huellas de barro por la entrada."
    voice "N67.mp3"
    nvle "El interior... devastado."

    voice "he9.mp3"
    he "No..."
    nvl clear
    voice "N68.mp3"
    nvle "Se arrodilla. Luego cae con todo el peso de su cuerpo. Comienza a sollozar."
    voice "he10.mp3"
    he "¿Por qué...?!"
    nvl clear
    voice "N69.mp3"
    nvle "Chancho se acerca con pasos inseguros. Quiere consolarla. Pero no sabe cómo. Frota su cabeza contra su brazo. No hay respuesta."
    voice "N1.mp3"

    voice "N70.mp3"
    nvle "Se aleja. Entra a la casa destruida. Cruza entre vidrios y muebles volcados. Encuentra una manta enredada entre los restos de un sillón."
    
    voice "N71.mp3"
    nvle "Chancho sale con la manta entre los dientes. Se acerca a Helena, que ya no llora. Solo respira fuerte, con los ojos perdidos."
    voice "N72.mp3"
    nvle "Chancho la cubre con torpeza. Luego se acuesta junto a ella. Su cuerpo toca apenas el suyo."


    ###### Chancho Día 4 ###############################
    #################################################
    scene bg casa chancho
    nvl clear
    voice "N73.mp3"
    nvle "Chancho, más pequeño. Hortensia lo baja de la camioneta. Está envuelto en una manta. Lo deja en la parte trasera de la casa, junto a las caléndulas."

    #show chancho at center 
    voice "mama11.mp3"
    ho "Por aquí estarás más seguro. Diviértete, sé libre."
    nvl clear
    voice "N74.mp3"
    nvle "Chancho la mira. No entiende todo, pero asiente con el cuerpo. Ella le acomoda la manta. Le da una palmada suave en la cabeza. Luego se va. "
    voice "N75.mp3"
    nvle "Chancho huele el lugar. Mira alrededor. Camina en círculos. Luego se aleja, adentrándose en los arbustos. La cueva lo espera."
    voice "N76.mp3"
    nvle "Chancho despierta primero. La manta se ha deslizado por su lomo. Se sacude. Mira a Helena, aún dormida, cubierta de tierra y lágrimas secas. Se acerca. La empuja con el hocico. Ella gruñe bajo."


    ch "Despierta. No puedes quedarte aquí. Hace frío."
    nvl clear
    voice "N77.mp3"
    nvle "Chancho la empuja de nuevo. Esta vez más fuerte. Helena gruñe."

    voice "he11.mp3"
    he "Ya basta... cerdo tonto..."
    nvl clear
    voice "N78.mp3"
    nvle "Chancho la jala del suéter. Ella forcejea. Se sienta de mala gana."
    voice "he12.mp3"
    he "¿¡Qué quieres ahora, huh!?"
    nvl clear
    voice "N79.mp3"
    nvle "No hay respuesta. Solo la mirada tierna de Chancho. {p=1.5} Ella suspira. {p=1.5} Se pone de pie con lentitud. Caminan."
    voice "N80.mp3"
    nvle "Helena entra. Chancho se queda en la entrada. Ella observa el caos. Se arrastra hasta el refrigerador. Lo abre. Saca una charola sellada. No la mira. Solo la agarra. Camina hacia su cuarto."
    voice "N81.mp3"
    nvle "Chancho se sienta fuera. Mira la puerta. Luego al pasillo. Espera."

    show HelenaSuicida 
    ""


    ###### Chancho Cuerpo ###############################
    #################################################
    scene bg cueva with slow_dissolve
    nvl clear
    voice "N82.mp3"
    nvle "Chancho espera.  {p=1.5} Día 1.  {p=1.5} Día 2. {p=1.5} Día 3."
    ch "Sigue sin moverse. Tal vez solo duerme mucho... como cuando llueve."
    nvl clear
    voice "N83.mp3"
    nvle "Chancho regresa a su cueva. Se acurruca."
    voice "N84.mp3"
    nvle "Chancho vuelve. La puerta de la casa está entreabierta."
    ch "Creo que ya salió."
    nvl clear
    voice "N82.mp3"
    nvle "Chancho entra con cautela. El aire huele extraño. Fétido."


    scene bg casa_blur with fade
    nvl clear
    voice "N86.mp3"
    nvle "Todo sigue revuelto. Pero ahora hay algo más."
    show bg sangrepiso
    voice "N87.mp3"
    nvle "Sangre en el piso. {p=1.5} Chancho retrocede."
    show ojosChancho
    voice "N88.mp3"
    nvle "Un cuerpo en el suelo."
    voice "N89.mp3"
    nvle "Se acerca de nuevo. Lo huele más profundamente. Sus ojos se agrandan."
    ch "No... No, tú no. Tú no."

    scene bg hortensiamuerta with dissolve
    nvl clear
    voice "N90.mp3"
    nvle "Es Hortensia. O lo que queda de ella. Mutada. Fracturada."
    voice "N91.mp3"
    nvle "Chancho se desploma. Llora. No con sonido. Solo con cuerpo."
    voice "N92.mp3"
    nvle "La empuja con la cabeza. Nada. Le raspa el brazo. Nada."
    voice "N93.mp3"
    nvle "Se acurruca junto a ella. Se queda ahí. No hay más."
    
    scene bg casa_blur with dissolve
    nvl clear
    voice "N94.mp3"
    play sound "audio/Foley/Estómago gruñendo.mp3"
    if persistent.audio_cues:
        $ Descripcion = "Se escucha el estómago de Chancho gruñendo"
    nvle "Chancho despierta en el mismo lugar. Helena no ha vuelto en días. Tiene hambre. Ya no hay comida. Mira el cuerpo. No lo toca. Sale."
    voice "N95.mp3"
    nvle "Chancho camina con pasos lentos. Busca comida o algo. El aire es húmedo. Más que otros días."
    scene bg funeral hoyo with fade
    nvl clear
    voice "N97.mp3"
    nvle "Pasa junto a la tumba de Hortensia. Algo brilla. Se detiene. Mira hacia el hueco."
    scene bg manomuerta with dissolve
    nvl clear
    voice "N98.mp3"
    nvle "Dentro, el cuerpo de Helena yace inerte. Brazo sobre el pecho. Las muñecas abiertas. {p=1.5} Sangre seca. {p=1.5}Hongos blancos brotan por las heridas. Apenas empieza a cubrirse."
    
    scene bg manomuertasegundo with dissolve
    nvl clear
    voice "N99.mp3"
    nvle "Chancho baja. Olfatea el cuerpo. Cierra los ojos."
    voice "N100.mp3"
    nvle "El sol comienza a bajar."


    ###### FINAL 4 Cerdo ############################
    #################################################
    
    $ final_arbol = True
    scene black with slow_dissolve
    show screen arbol_screen with fade1
    ""
    ""
    ""
    ""
    return


#####################################################
## RUTA FLASHBACKS ##################################
#####################################################
label flash:
    $ ui_depre = True
    $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)
    hide screen arbol_screen
    $ principal_flag = False
    $ novias_flag = False
    $ coqueteo_flag = False
    $ flash_flag = True
    $ secuestro_flag = False
    $ salvar_flag = False
    $ caminoa_flag = False
    $ caminob_flag = False


    ###### Día 1 Depresión ############
    #################################################
    scene bg sillon with fade2
    nvl clear
    voice "N101.mp3"
    nvle "En la habitación, en el centro, Helena permanece sentada en el colchón, la nota de su madre apretada entre los dedos."
    show i_he_decadencia at leftdown
    he "No era tan difícil confiar en mí, mamá. No para esto."
    scene bg hortensia
    nvl clear
    voice "N102.mp3"
    nvle "Con un grito ahogado, lanza el marco de la foto contra la pared. El vidrio se rompe con un crujido seco. Se levanta de golpe, respira agitada. Empieza a derribar objetos: abre cajones y los vacía, tira almohadas, golpea la cabecera. Patea el buró con fuerza."
    show helena enojo at leftdialogue
    he "¡Tercas! ¡Eso dijiste! ¡Claro que lo somos! ¡Pero esto no se hace así, mamá!"
    nvl clear
    voice "N103.mp3"
    nvle "Sollozos contenidos la interrumpen. Cae de rodillas entre los restos, jadeando, con los puños cerrados."
    scene bg hortensia
    nvl clear
    voice "N104.mp3"
    nvle "Un sonido. Golpes suaves. Alguien toca la puerta trasera que da al jardín."
    
    ##### Decision
    menu:
        "Abro la puerta":
            voice "N105.mp3"
            "Helena se pone de pie, tambalea"
            

        "Agarro la foto":
            show fotofam at centerup
            voice "N106.mp3"
            "Helena se pone de pie y agarra la foto de su mamá"
            he "Me hubiera gustado que te despidieras en persona."
            hide fotofam
            
    nvl clear
    voice "N107.mp3"
    nvle "Vuelven a tocar la puerta. Helena se pone de pie, tambaleante."
    voice "N108.mp3"
    nvle "Sale del cuarto."

    scene bg casa exterior with fade3
    nvl clear
    show chancho sentado at rightdown
    voice "N109.mp3"
    nvle "Cruza la cocina. Abre la puerta trasera con un tirón brusco. El cerdo está allí, con su overol sucio."
    he "No. No hoy."
    voice "N110.mp3"
    nvle "Le cierra la puerta sin dudar."
    scene bg hortensia with fade3
    nvl clear
    voice "N111.mp3"
    nvle "La luz blanca del baño la deslumbra. Abre la llave. Se enjuaga la boca una y otra vez, cepillo en mano. Escupe. Siente náuseas."
    scene bg vomito sec
    he "No se va... no se va..."
    
    nvl clear
    voice "N112.mp3"
    nvle "Vuelve a cepillarse, con desesperación. El sabor sigue ahí. Arcadas. Se inclina sobre la taza. Vomita, pero no sale nada. Solo espasmos vacíos. Se queda ahí, respirando con dificultad, las manos aferradas al borde del inodoro."
    scene bg hortensia blur with fade3
    nvl clear
    show helena crisis at leftdown
    voice "N113.mp3"
    nvle "Lentamente, se desliza hacia el suelo, agotada. Se abraza las piernas. Y llora. Sin palabras. Solo el sonido de su respiración entrecortada, acompasado por el eco lejano de los golpecitos que Chancho aún hace en la puerta del jardín."


    ###### Flash primera vez ##########################
    #################################################
    scene bg magenta with fade1
    play sound "audio/Ambientacion/IN 1.mp3"
    nvl clear
    voice "N114.mp3"
    nvle "Las paredes grises y sin pintar absorben la poca luz del sol que se cuela por la ventana. El aire es tibio y huele a aceite recalentado. Helena, con apenas ocho años, come sentada frente a un plato de princesas. Sus padres, Hortensia y Hugo, cenan en silencio."
    show heleniña
    voice "Nina_10.mp3" 
    he "¡AAAAAAH!"
    nvl clear
    voice "N115.mp3"
    nvle "El grito resuena como un disparo. Hortensia se levanta de golpe, tirando el tenedor. Hugo se queda inmóvil al principio, luego corre a abrazar a su hija. Helena está tiesa, los ojos en blanco, el cuerpo tembloroso. Hortensia cae de rodillas frente a ella."
    voice "mama12.mp3"
    ho "Mi niña... mi niña..."
    nvl clear
    voice "N116.mp3"
    nvle "Helena rompe en llanto. Hugo la aprieta contra su pecho."
    voice "Nina_11.mp3" 
    he "Luces... muchas luces... y una cama... había pitidos... alguien lloraba."
    hide heleniña
    show bg papas dos with fade3
    voice "mama13.mp3"
    ho "Mi niña."
    nvl clear
    voice "N117.mp3"
    nvle "Los padres se miran confundidos."
    scene bg hortensia blur with fade2
    nvl clear
    voice "N118.mp3"
    nvle "La mesa está servida. Carne y ensalada. Helena empieza a comer. Entra de nuevo en trance. Hortensia la abraza con cuidado, acariciándole el cabello. Hugo mira la carne que queda en el plato de su hija. Suda. Toma un pedazo. Lo observa. Lo huele."
    scene bg boca with fade2
    nvl clear
    voice "N119.mp3"
    nvle "Sin decir nada, se agacha frente a la niña."
    voice "Hugo13.mp3"
    hu "A ver, abre tu boquita."
    nvl clear
    voice "N120.mp3"
    nvle "Helena obedece sin pensar. Mastica. Dos segundos después, las pupilas se le dilatan. El cuerpo se tensa. El trance la reclama."
    
    scene bg amarillo heleniña
    nvl clear
    voice "Nina_12.mp3" 
    he "Cortinas blancas... una viejita llorando... pitidos... ¡La enfermera ya viene!"
    voice "N121.mp3"
    nvle "Helena se calma. Esta vez no hay llanto. Solo cansancio. Hugo la mira como si hubiera encontrado oro. Se incorpora."
    
    scene bg rojo with fade3
    nvl clear
    show i_hu at leftdialogue
    voice "Hugo5.mp3"
    hu "¡Hortensia! ¡Tiene un don! ¡¿No lo ves?! ¡Puede ver a los muertos!"
    show i_ho at rightdialogue
    voice "N122.mp3"
    nvle "Hugo toma la mano de Hortensia"

    voice "Hugo6.mp3"
    hu "Hay gente que pagaría por esto."
    voice "mama14.mp3"
    ho "No vamos a lucrar con esto."
    voice "Hugo7.mp3"
    hu "Esto no es sobre el dinero, es sobre ayudar, Hortensia. La gente necesita saber... ¡Y nosotros también!"
    voice "mama15.mp3"
    ho "¿Y hacer de nuestra hija una médium?"
    voice "Hugo8.mp3"
    hu "Solo en lo que me alivio de la espalda."
    nvl clear
    voice "N123.mp3"
    nvle "Ella se aleja cargando a su hija. Entra al cuarto y cierra la puerta. Se acuesta con Helena sin decir una palabra."
    play sound "audio/Ambientacion/IN 1.mp3"


    ###### Día 2 Depresión ####################################
    #################################################
    show lavabo with fade1
    nvl clear
    voice "N124.mp3"
    nvle "El agua del lavabo sigue corriendo. Helena deja de llorar. Se incorpora. Tiene los ojos hinchados, pero la mirada firme."
    voice "N125.mp3"
    nvle "Sale del baño."

    scene bg hortensia with fade1
    nvl clear
    show helena decadencia at leftdown
    voice "N126.mp3"
    nvle "Entra a su habitación y azota la puerta."
    voice "N127.mp3"
    nvle "Se lanza a la cama. "
    voice "N128.mp3"
    nvle "La casa se queda en silencio. Las horas pasan. En la habitación, solo el sonido suave de una respiración rota acompaña la oscuridad. Helena, entre la fatiga y los recuerdos, al fin se queda dormida."


    ###### Flash Hongo #################################
    #################################################
    scene bg bosque with fade1
    nvl clear
    play sound "audio/Ambientacion/IN 1.mp3"
    voice "N129.mp3"
    nvle "El cielo está cubierto por nubes grises. Un bosque espeso y verde respira en silencio. La tierra está húmeda, cubierta de hojas viejas y ramas rotas. Los hongos brotan en grupos diminutos, ocultos entre la maleza. Todo está cubierto por una niebla baja que suaviza los contornos."
    show heleniña at centerleft with easeinleft
    voice "N130.mp3"
    nvle "Helena camina junto a su madre, Hortensia. Ambas llevan canastas de mimbre vacías y los zapatos llenos de barro. Hortensia se detiene y se arrodilla junto a un tronco caído."
    show i_ho at rightdialogue with easeinright
    voice "mama16.mp3"
    ho "Estos de aquí... son buenos. Mira las láminas por debajo, como costillas. Son como los que comimos el otro día."
    nvl clear
    voice "N131.mp3"
    nvle "Helena se agacha también. Sus dedos temblorosos rozan los hongos blancos. Son como orejas blandas pegadas a la madera. Hortensia la observa con paciencia."
    voice "mama17.mp3"
    ho "No debemos comer cualquier hongo porque no todos son amigos."
    voice "N132.mp3"
    nvl clear
    nvle "Helena está sola ahora. La canasta casi le cuelga del brazo. Canta una melodía suave mientras avanza entre ramas. Sus pies descalzos chapotean en el barro. Observa cada rincón con cuidado."

    voice "Nina_13.mp3" 
    he "Hoy no hay hongos..."
    nvl clear
    voice "N133.mp3"
    nvle "Se detiene de golpe. Algo ha llamado su atención."
    scene bg honguitos with fade3
    nvl clear
    voice "N134.mp3"
    nvle "En la base de un árbol viejo, medio podrido, hay un hongo distinto. Es blanco, con forma de abanico. Brilla, húmedo, como si acabara de despertar de un sueño largo. Crece sobre una masa de huesos diminutos, cubiertos de musgo."
    voice "N135.mp3"
    nvle "Helena se agacha. Lo observa con curiosidad. No parece temerosa. Lo arranca con cuidado y lo guarda en su canasta."
    voice "N136.mp3"
    nvle "Los hongos crecen y forman un paisaje precioso."
    play sound "audio/Ambientacion/IN 1.mp3"


    ###### Ansiedad #################################
    #################################################
    show reloj with fade1
    nvl clear
    voice "N137.mp3"
    nvle "Helena se despierta bruscamente en su cama. Mira hacia un reloj digital sobre el buró: 6:13 a.m. No ha dormido bien. Camina hacia la puerta de su cuarto, apoya la mano en la perilla y la gira."
    voice "N138.mp3"
    nvle "Abre la puerta. Da un paso hacia el pasillo, pero al girar la cabeza ve el baño. {p=1.5} Se queda petrificada."
    voice "N139.mp3"
    nvle "La luz del baño sigue encendida, parpadeando. La imagen de anoche la golpea como un muro. Las arcadas, el piso frío, el sabor en la boca. Retrocede. La respiración se le acelera."

    scene bg amarillo heleniña with dissolve
    play sound "audio/Ambientacion/IN 1.mp3"
    nvl clear
    voice "Nina_14.mp3" 
    he "No... no otra vez... por favor..."
    play sound "audio/Ambientacion/IN 1.mp3"
    scene bg hortensia blur with dissolve
    show helena crisis at leftdown
    nvl clear
    voice "N140.mp3"
    nvle "Cae de rodillas. Se abraza a sí misma. El pecho sube y baja con violencia. Gime bajo, como si intentara ocultarse incluso de su propio cuerpo. Y entonces, se quiebra."


    ###### princesa #################################
    #################################################
    $ ui_flash = True
    label FlashUI_label:  
        $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)
        hide screen arbol_screenS
        $ principal_flag = False
        $ novias_flag = False
        $ coqueteo_flag = False
        $ flash_flag = False
        $ secuestro_flag = True
        $ salvar_flag = False
        $ caminoa_flag = False
        $ caminob_flag = False

        hide screen arbol_screen
    
    nvl clear
    show carneVelas
    play sound "audio/Ambientacion/IN 1.mp3"
    voice "N141.mp3"
    nvle "La cocina está en penumbra. Una vela encendida parpadea sobre la mesa. Helena come un guiso sencillo. Hortensia canta bajito mientras lava algo en el fregadero."
    voice "N142.mp3"
    nvle "De pronto, Helena se queda quieta. Parpadea varias veces. Su cuerpo se arquea levemente hacia adelante. La vela se agita."
    voice "N143.mp3"
    nvle "La vela se apaga de golpe."
    
    scene bg amarillo heleniña
    nvl clear
    voice "N144.mp3"
    nvle "Cada vez que come carne, Helena entra en un trance. La llevan con doctores, hacen estudios, pruebas, pero no hay respuestas."
    scene bg sacerdoniña 
    nvl clear
    voice "N145.mp3"
    nvle "Un pequeño altar hecho con velas, flores secas y telas colgantes. Todo enmarcado con una tela morada desteñida. Hugo, sonriente, acomoda sillas plegables frente al altar."
    voice "N146.mp3"
    nvle "Helena, con un vestido de princesa manchado en la parte baja, está sentada en una silla de madera al centro. El cabello recogido en una media corona de flores plásticas. Sus ojos están vacíos."
    voice "N147.mp3"
    nvle "Frente a ella, una mujer de luto, llorando desconsolada, le entrega un pequeño trozo de carne cruda en un platito."
    voice "xim2.ogg"
    ma "Por favor... solo quiero saber si me escuchó antes de irse."
    nvl clear
    voice "N148.mp3"
    nvle "Helena mastica sin resistencia. Hugo se para detrás de ella, una mano sobre su hombro. La carne entra. La visión llega. El cuerpo de la niña se sacude. Las pupilas se dilatan. El aire se vuelve espeso."

    voice "Nina_15.mp3" 
    he "Dijo... dijo que sí. Que escuchó... y que no te guarda rencor..."
    scene bg dinero with fade3
    nvl clear
    voice "N149.mp3"
    nvle "La mujer rompe en llanto. Hugo sonríe satisfecho, mientras mete el sobre de dinero en el bolsillo de su pantalón."
    voice "N150.mp3"
    nvle "Hugo le coloca un collar de flores a Helena mientras le dice:"
    
    voice "Hugo9.mp3"
    hu "Eres un puente, mi reina... eres la llave."
    voice "Nina_16.mp3" 
    he "Llave no. Tengo hambre..."
    voice "Hugo10.mp3"
    hu "Come otro bocado. Y sonríe. La gente viene por ti."
    scene bg boca with dissolve
    nvl clear
    voice "N151.mp3"
    nvle "Helena obedece, tragando sin gusto."
    play sound "audio/Ambientacion/IN 1.mp3"
    
    ###### Ansiedad 2 #################
    #################################################
    scene bg ventanarayo with fade2
    nvl clear
    voice "N152.mp3"
    nvle "Helena, acurrucada frente a la puerta de su cuarto, llora sin fuerzas. Sus dedos se clavan en los brazos. Hiperventila. La luz del baño titila una vez más."
    scene bg casa
    nvl clear
    show helena decadencia at leftdown
    voice "N153.mp3"
    play sound "audio/Foley/Ventana rompiendose.mp3"
    nvle "Un estruendo. Una ventana rompe en otra parte de la casa. Algo pesado cae al suelo. Silencio."
    play sound "audio/Foley/Estruendo 2.mp3"
    voice "N154.mp3"
    nvle "Helena no se mueve. Otra pisada. Algo corre. Un quejido bajo."
    
    show chancho at center
    voice "N155.mp3"
    nvle "El cerdo aparece en el pasillo, cubierto de polvo y con el overol rasgado. Lleva una maceta rota en las manos."
    voice "N156.mp3"
    nvle "Se detiene al ver a Helena hecha trizas en el suelo."

    ch "Oink..."

    ##### Decisión 
    menu:
        "Le digo algo":
            he "¿Sabes qué? Desordena lo que quieras. Ya no importa."

        "Lo ignoro":
            ""
    
    nvl clear
    voice "N157.mp3"
    nvle "Helena apenas lo mira. Sus ojos están vidriosos, las lágrimas aún no se han secado. Se levanta tambaleante, entra de nuevo a su cuarto, y cierra la puerta lentamente."
    ch "Oink..."
    nvl clear
    voice "N158.mp3"
    nvle "Helena está tendida sobre la cama, inmóvil, con el rostro hacia la pared. Su respiración es leve, apenas perceptible. El sueño llega no por descanso, sino por agotamiento."


    ###### Choza ####################################
    #################################################
    scene bg altar with fade1
    nvl clear
    play sound "audio/Ambientacion/IN 1.mp3"
    voice "N159.mp3"
    nvle "Helena, niña de ocho años, camina con un vestido de princesa arrastrándose por el lodo. El bosque está distorsionado, como si la niebla escondiera cosas que no se atreven a mostrarse por completo."
    voice "N160.mp3"
    nvle " De los árboles cuelgan trozos de carne envueltos en listones. Hay velas encendidas sobre charcos, flotando como ofrendas."
    voice "N161.mp3"
    nvle "A lo lejos, una choza de madera hecha de sillas rotas, cortinas deshilachadas y huesos. Dentro, una silueta familiar: Hugo."
    scene bg rojo hugo with fade3
    nvl clear
    voice "N162.mp3"
    nvle "Helena observa que frente a él, otra Helena está sentada con una bandeja en el regazo. Come sin masticar. El cuerpo le tiembla, pero sus ojos no parpadean."

    voice "Hugo11.mp3"
    hu "Come un poco más, princesa. Así ayudas al mundo..."
    voice "Nina_17.mp3" 
    he "Ya no quiero papá..."
    scene bg altar with fade3
    nvl clear
    voice "N163.mp3"
    nvle "Hugo se levanta. Camina sobre las velas sin apagarlas. Se arrodilla frente a ella y le limpia la boca con un billete ensangrentado. El bosque se encoge. Los árboles de carne envuelven la choza."
    voice "N164.mp3"
    nvle "Helena sigue observando desde fuera y se escucha un canto de rezo. Las velas de los charcos se apagan."
    voice "N165.mp3"
    nvle "El cielo está gris y todavía no canta ningún gallo. Hortensia camina decidida con un machete en la mano hacia la choza. El vestido que lleva está manchado con algo que parece óxido. Se acerca al santuario. Los trapos colgantes se agitan como si supieran lo que viene."

    scene bg amarillo papas with fade2
    nvl clear
    voice "mama18.mp3"
    ho "Esto se acabó..."
    nvl clear
    voice "N166.mp3"
    nvle "Rompe con el machete el primer poste. Las velas se caen. El suelo cruje. Rompe telas, rompe bancas. Los gritos de Hugo se acercan."

    voice "Hugo12.mp3"
    hu "¡¡Estás loca, mujer!!"
    nvl clear
    voice "N167.mp3"
    nvle "La agarra del brazo. Le arrebata el machete. El rostro de Hortensia cambia de rabia a miedo. Hugo la abofetea. El sonido resuena en todo el sueño como una campana de hierro."
    voice "N168.mp3"
    nvle "Aparece Helena de la oscuridad."
    show heleniña at righter
    voice "Nina_18.mp3" 
    he "¡NO, MAMI!"
    scene bg amarillo hugo
    nvl clear
    voice "N169.mp3"
    nvle "El grito hace temblar el sueño. La escena se ralentiza. Hugo ahora es una figura grotesca, amorfa. Tiene múltiples brazos. Una de sus manos intenta alcanzar a Helena. Hortensia toma el machete del suelo, lo hunde en la espalda de su esposo."
    voice "N170.mp3"
    nvle "Helena, empuja el machete más profundo. Su vestido está destrozado. Hortensia no logra reaccionar. El cuerpo de Hugo se desvanece como si estuviera hecho de humo denso."
    scene bg hortensia helena with fade3
    voice "Nina_19.mp3" 
    he "Ahora ya podremos ser libres, ¿verdad mami?"
    nvl clear
    voice "N171.mp3"
    nvle "Los rezos vuelven. Pero ahora vienen desde dentro de Helena. Voces sin cuerpo. Voces rotas."
    voice "N172.mp3"
    nvle "Ahora el bosque se ve distinto. Es el mismo lugar, pero con tonos lúcidos, enfermos. Las ramas están cubiertas de carne cruda. Los hongos gigantes palpitan como corazones abiertos."
    voice "N173.mp3"
    nvle "Helena se encuentra de pie, con las manos y la boca manchadas de sangre. Sus ojos brillan como brasas."
    
    voice "Nina_20.mp3"   
    he "No quiero ser esto..."
    play sound "audio/Ambientacion/IN 1.mp3"


    ###### Secuestro Flashbacks ####################################
    #################################################
    scene bg hortensia with fade2
    nvl clear
    show helena decadencia at leftdown
    voice "N174.mp3"
    nvle "Helena se despierta de golpe, cubierta de sudor. La habitación está oscura y no hay un solo sonido. Se sienta. Tiembla. Mira sus manos. No hay sangre. "
    voice "N175.mp3"
    nvle "Se levanta lentamente. Camina al escritorio. Abre un cajón. Saca una navaja oxidada, pequeña, usada para jardinería. La coloca sobre la mesa. A su lado, una nota en blanco."
    scene bg rojo suicidio with fade2
    nvl clear
    he "No queda nada. Mi madre está muerta. Yo también..."
    scene bg hortensia with fade2
    nvl clear
    show helena suicida at leftdown
    nvl clear
    voice "N176.mp3"
    nvle "Se sienta frente a la hoja. Mira fijamente la navaja. La toma entre los dedos. Sus ojos se empañan."
    show secuaz tlacuache at centerup
    voice "N177.mp3"
    play sound "audio/Foley/Estruendo 1.mp3"
    nvle "Entonces, un estruendo. Se escucha a alguien caer pesadamente en la sala y luego a otro, . Voces graves se escuchan, acompañadas del crujido de botas y muebles siendo movidos."
    show secuaz jaguar at left
    voice "Sec4.mp3"
    s1 "Está aquí. Revisen todo."
    hide helena suicida
    voice "Secuaz7.mp3"
    show secuaz aguila at right
    s2 "Recuerden que la quiere viva."
    scene bg hortensia with dissolve
    nvl clear
    voice "N178.mp3"
    nvle "Helena reacciona, pero tarde. Gira hacia la puerta, pero ya se abre violentamente. Un híbrido la toma del brazo."

    he "¡Suéltame!"
    nvl clear
    voice "N179.mp3"
    nvle "Otro hombre entra con una jeringa. Helena forcejea, pero está demasiado débil. La jeringa entra en su cuello. Su cuerpo se ablanda."

    #ch "¡OIIIIIIINK!"


    ###### Dra. Elodia ####################################
    #################################################
    scene bg lab
    nvl clear
    show helena secuestro at leftdialogue
    voice "N180.mp3"
    nvle "Helena despierta desorientada encerrada en una celda. El cuarto es blanco, clínico, sin ventanas. Solo una camilla y una mesa metálica. La luz es fría, casi azul. Se levanta con dificultad."
    show i_el_tres at right with easeinright
    voice "Helodia_12.mp3"
    el "Buenos días, Helena."
    he "¡¿Dónde estoy?!"
    el "Relájate, estás en buenas manos. Soy la Dra. Elodia Rivas. Un placer conocerte."
    nvl clear
    voice "N181.mp3"
    nvle "Elodia deja la carpeta sobre la mesa. La observa un momento."
    voice "N182.mp3"
    nvle "Elodia se mantiene de pie, impasible, con las manos entrelazadas frente a ella. Su rostro no muestra ni desprecio ni ternura. Solo un estudio meticuloso."

    he "Esto... no es un hospital."
    el "Correcto. Es un laboratorio."
    nvl clear
    voice "N183.mp3"
    nvle "Luego presiona un botón junto a la puerta. Una pantalla desciende del techo. La imagen que aparece es la de Hortensia, sentada en una celda estéril. La mujer murmura algo que el audio no permite oír."

    el "Tu madre resistió el virus durante más tiempo del esperado."
    nvl clear
    voice "N184.mp3"
    nvle "Helena siente un nudo en la garganta. Vuelve a mirar la pantalla. La imagen de Hortensia desaparece."
    he "Pero mi madre estaba sana antes de desaparecer."
    el "Ay querida, no estás entendiendo. Tu madre no llegó aquí por voluntad propia. Yo no trabajo con voluntarios. ¿Eres tú una voluntaria?"
    nvl clear
    voice "N185.mp3"
    nvle "Entra un secuaz y ata a Helena a la camilla."
    
    he "¡Aaaargh!"
    nvl clear
    voice "N186.mp3"
    nvle "Elodia entra a la celda."
    el "Le pedí a tu madre que me ayudara con un encargo entrando al depósito durante una entrega, no sospechó nada. Estaba tan preocupada por ayudar..."
    el "Tanta amabilidad. Tanta ingenuidad. Fue decepcionante."
    he "Pensé que buscabas al cerdo."
    el "También, pero tu madre no cooperó, y hay algo en ti que es clave para la investigación."
    scene bg jeringa
    nvl clear
    voice "N187.mp3"
    nvle "Elodia toma una inyección de su bata y la inyecta. Helena voltea los ojos en blanco. Su respiración se vuelve pesada. Tiembla. Se desmorona."
    voice "N188.mp3"
    nvle "Dos hombres entran. Uno la toma de los brazos, el otro de las piernas."
    el "Llévenla a la celda 64. No la alimenten en 3 días. Veamos cómo reacciona el virus en su cuerpo."
    
    jump pierde


#####################################################
## FINAL 3 Novias ###################################
#####################################################

label novias:
    $ ui_adara = True
    $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 16)
    hide screen arbol_screen
    $ principal_flag = False
    $ novias_flag = True
    $ coqueteo_flag = not coqueteo_flag
    $ flash_flag = False
    $ secuestro_flag = False
    $ salvar_flag = False
    if final_arbol:
        $ caminoa_flag = not caminoa_flag
        $ caminob_flag = not caminob_flag
    ###### Adara Enterrar ###########################
    #################################################

    scene bg noche with fade2
    nvl clear
    voice "N189.mp3"
    nvle "Con ayuda de Chancho, Helena entierra la caja y le da dos palmaditas al pequeño en la cabeza a modo de agradecimiento."
    show i_ad_tres at right
    voice "Adara_84.mp3"
    ad "¿Estás bien con dejar las cosas así, Lena?"
    show i_he_tres at leftdialogue

    ##### A y B ###################################
    menu:
        "Tengo que estar bien, voy a estar bien.":
            voice "Helena_205.mp3"
            he "Tengo que estar bien, voy a estar bien."
            $ caminoa_flag = True
            $ caminob_flag = False
            voice "Adara_85.mp3"
            ad "Aquí estaré para apoyarte, Lena."
            nvl clear
            voice "N190.mp3"
            nvle "La rubia la abraza de lado. Helena se tensa ante la cercanía de Adara, se sonroja, pero se mantiene en silencio."
            voice "Adara_86.mp3"
            ad "Somos amigas a final de cuentas. Sabes que siempre estaré para ti."
            scene bg magenta helena with dissolve
            nvl clear
            voice "N190.mp3"
            nvle "Adara aprieta su abrazo y se separa de Helena sin más y se pone a acomodar un espacio con hojas para dormir en el bosque. Mientras tanto en la mente de Helena sólo resuena la palabra AMIGAS una y otra vez, se queda en blanco, pero al ver como la rubia parece no estar afectada como ella, suspira desanimada y se pone a ayudarla con las hojas."
            he "Sí... amigas."
            scene bg noche with dissolve
            show i_he_tres at leftdialogue
            voice "Helena_144.mp3"
            he "Perdón, sé que he sido grosera contigo."
            show i_ad_tres at right
            voice "Adara_87.mp3"
            ad "No lo has sido, Lena."
            scene bg noche
            nvl clear
            voice "N191.mp3"
            nvle "Se acomodan de espaldas en el suelo cerca de la fogata que ya se ha extinguido y el sueño llega sin permiso."

        "No lo sé, Ara.":
            $ caminob_flag = True
            $ caminoa_flag = False
            scene bg noche
            nvl clear
            show i_he_decadencia at leftdown with dissolve
            he "Si te soy sincera siento que me voy a arrepentir, pero esto me rebasa y ya no sé qué hacer... tengo miedo."
            show i_ad_tres at right
            voice "Adara_88.mp3"
            ad "Ay Lena..."
            voice "N193.mp3"
            nvle "Adara abraza con fuerza a Helena, la castaña aprovecha y hunde su cara en el pecho de Adara, el silencio las invade. La pareja se separa ligeramente sin romper el abrazo, se ven a los ojos y Adara limpia las pocas lágrimas que salen de los acuosos ojos de Helena, la castaña la ve con la cara contraída."
            voice "Adara_89.mp3"
            ad "No llores Lena, está bien tener miedo. Además no estás sola, tienes a chancho... y me tienes a mí."
            hide i_he_decadencia
            scene bg magenta helenadara with dissolve
            nvl clear
            voice "N194.mp3"
            nvle "Helena la mira un poco sorprendida al principio, después sonríe ligeramente."
            he "¿Pero me vas a besar o solo me vas a conso...?"
            scene bg beso with dissolve
            nvl clear
            voice "N195.mp3"
            nvle "Adara no lo piensa dos veces, con la mano que mantenía su abrazo, aprieta su cintura hacia ella y la otra la toma por la nuca para acercarla contra su labios."
            voice "N196.mp3"
            nvle "Helena es silenciada a media palabra por el beso tan brusco que le da la rubia, está tan impactada por la intensidad del beso que intenta separarse de ella empujando la cadera de Adara, sin embargo, Adara se rehúsa a soltarla y termina aprisionando a Helena contra un árbol cercano mostrando su top ajustado y provocando que se separen un momento."
            voice "N197.mp3"
            nvle "Helena se queda admirando el físico torneado de la rubia haciendo que su ritmo cardíaco aumente y acerque su cadera. Adara toma el mentón de Helena con una de sus manos y la guía hasta su rostro."
            scene bg noche
            nvl clear
            show i_ad_tres at right with dissolve
            voice "Adara_90.mp3"
            ad "¿Te sigo besando o ya puedo seguir apoyándote?"
            show i_he_tres at leftdialogue with dissolve
            he "Ara, shhhhh."
            voice "N198.mp3"
            nvle "Helena se pone de puntas y le planta un suave beso a Adara. Adara se separa de Helena sin más y se pone a acomodar un espacio con hojas para dormir en el bosque. "
            nvl clear
            scene bg magenta helena with dissolve
            nvl clear
            voice "N199.mp3"
            nvle "Mientras tanto en la mente de Helena sólo resuena la palabra NOVIAS una y otra vez, se queda en blanco, y se pone a ayudarla con las hojas."
            scene bg noche
            nvl clear
            he "No me voy a ir a ningún lado. También iría contigo a cualquier parte."
            voice "N200.mp3"

            nvle "Se abrazan en el suelo y el sueño llega sin permiso."

    ###### AB

    ###### Secuestro de Chancho #####################
    #################################################
    scene bg calle with fade1
    nvl clear
    voice "N201.mp3"
    
    nvle "Los tres van llenos de hojas y lodo seco caminando por la banqueta, el pequeño Chancho como siempre va en la delantera, seguido de Helena y justo detrás Adara, que va más feliz y relajada de lo normal."

    if caminoa_flag:
        show i_ad_tres at right
        voice "Adara_91.mp3"
        ad "¿Entonces somos amigas?"
        show i_he_tres at leftdialogue
        he "Sí, ¿qué más? Tanta carne te está atrofiando el cerebro, Ara."
    

    if caminob_flag:
        show i_ad_tres at right
        voice "Adara_92.mp3"
        ad "¿Entonces volvimos?"
        show i_he_espalda at leftdialogue
        he "Tanta carne te está atrofiando el cerebro, Ara."
    
    
    show i_ad_tres at right with easeinright
    voice "Adara_93.mp3"
    ad "No hay que estar mucho tiempo en tu casa, hay que volver a la mía pronto."
    
    ##### Decisión 
    menu:
        "¿No quieres descansar un poco?":
            he "¿No quieres descansar un poco?"
            he "Anoche dormimos en el bosque."

        "Sí, solo voy a empacar.":
            he "Sí, solo voy a empacar."
   
    voice "Adara_94.mp3"
    ad "Va, después de eso nos vamos."

    scene bg casa exterior with fade3
    nvl clear
    voice "N202.mp3"
    nvle "Chancho es el primero en llegar a la casa, dirigiéndose directamente a las caléndulas de Hortensia. Helena está por llegar a su casa y de repente llega una van blanca polarizada."
    voice "N203.mp3"
    nvle "Alertadas por el ruido Adara y Helena corren hacía un callejón mientras ven con horror como bajan dos hombres de la van y Chancho es levantado del suelo y metido en el vehículo."
    voice "N204.mp3"
    nvle "La van acelera de reversa y sale de cuadro. Las chicas se pierden en el bosque cercano a la casa de Helena."
    scene bg bosque dia with fade2
    nvl clear
    voice "N205.mp3"
    nvle "Adara entra con cuidado al lugar, Helena va detrás de Adara. La rubia revisa con cuidado que la casa esté sola."
    show i_ad_deterioro at leftdown with easeinleft

    voice "Adara_95.mp3"
    ad "¡Se llevaron a Chancho!"
    show i_he_deterioro at centerup with easeinright
    he "Apenas anoche escapamos y ya saben dónde vivo."
    voice "Adara_96.mp3"
    ad "Esos hombres están detrás de esto."
    he "Maldición, nos alcanzaron muy rápido."
    he "Debemos escapar del pueblo, es cuestión de tiempo para que nos alcancen. No me siento segura ya aquí."
    voice "Adara_97.mp3"
    ad "Podemos ir a mi casa, ellos no saben de mí. Nos esconderemos en lo que nos vamos."
    nvl clear
    nvle "Helena la voltea a ver triste, se endereza para quedar cara a cara con Adara, asiente."
    if caminob_flag:
        voice "N207.mp3"
        nvle "Adara le da un corto beso"


    ###### Pelea ###############################
    #################################################
    scene bg adara casa with fade3
    nvl clear
    voice "N208.mp3"
    nvle "Llegan a casa de Adara y Helena sigue en shock mirando hacia el suelo."
    show i_he_tres at leftdialogue
    he "Deberíamos descansar un poco."
    show i_ad_enojada at right
    voice "Adara_98.mp3"
    ad "Reacciona, Helena. Por favor. Tenemos que escapar ya, antes de que se les ocurra regresar por nosotras. No podemos quedarnos aquí a esperar que las cosas se calmen, este lugar ya no es seguro."
    voice "Adara_99.mp3"
    ad "Si entendí bien todo, sólo les importa el puerco, entonces con suerte ya no nos molestarán más ahora que lo tienen. Debemos irnos."
    
    ##### Decisión 
    menu:
        "¿Cómo puedes decir eso tan tranquilamente?":
            hide i_ad_enojada
            hide i_he_tres
            show i_he_lateral at left
            show i_ad_frente at right
            he "¿Cómo puedes decir eso tan tranquilamente?"
            he "¿Qué no ves lo que pasa? Sobrevivimos a costa de un pequeño."
            voice "Adara_100.mp3"
            ad "Yo también me encariñé de Chancho, Helena, pero estoy pensando en sobrevivir."
    
        "Adara, por Dios, ¡se llevaron a Chancho!":

            hide i_he_tres
            show i_he_lateral at left
            he "Adara, por Dios, ¡se llevaron a Chancho!"
            he "¿Quieres que me preocupe por escapar como si lo de hace rato no hubiera pasado? ¿Acaso no está en tus planes rescatarlo?"
            voice "Adara_101.mp3"
            ad "¿Y qué, nos maten? Si de verdad querías enfrentar esto, no hubieras enterrado la caja. Ahora ya es tarde y yo estoy pensando en sobrevivir."
    
    nvl clear
    voice "N209.mp3"
    nvle "Helena retira con brusquedad la mano de Adara, mientras la ve sin emoción alguna en sus ojos. Helena se levanta en silencio dejando a la rubia sin palabras. Se acerca a la ventana de la sala, recarga su mano en el vidrio y ve el jardín de Adara."
    he "No hicimos nada, y aún así en lo único que nos preocupamos sigue siendo en nosotras. ¡¿Qué no ves?! ¡Somos unas malditas egoístas!"
    voice "Adara_102.mp3"
    ad "¿Y qué preferías que hiciera? Dejarte correr a salvar al niño solo te hubiera llevado a tu muerte, Lena. Esa gente no se anda con rodeos, entiende."
    he "¿Y de qué me sirvió haber evitado morir? Me siento horrible por dentro, Ara. Todavía no terminó mi luto por mi madre y ¿ahora esto? Esta es una maldita señal, yo no-"
    nvl clear
    voice "N222.mp3"
    nvle "Adara le tapa la boca a Helena, está con la cabeza gacha y sólo siente cómo las lágrimas de Helena corren por su mano y algunas se deslizan por su antebrazo. El silencio las invade, Helena sólo cierra los ojos sin resistirse al bloqueo de Adara."
    
    voice "Adara_103.mp3"
    ad "Basta Helena, no digas más... por favor. Me duele verte así, escucharte así, sólo... para, por favor."
    nvl clear
    voice "N223.mp3"
    nvle "Helena se mantiene quieta, Adara quita su mano y procede a tomar sus manos para posarlos sobre su corazón."
    voice "Adara_104.mp3"
    ad "Sé que estás pasando por mucho ahorita, pero por favor no te rindas aún. Sé que no es mucho, pero me tienes a mí."
   
    if caminoa_flag:
        hide i_he_lateral
        show i_he_espalda at leftdialogue
        he "Adara, no te confundas. No sabes cómo me afectó lo que me hiciste."

    if caminob_flag:
        hide i_he_lateral
        show i_he_espalda at leftdialogue
        he "¿Acaso crees que por lo que hicimos anoche ahora tienes el derecho de decir eso? ¿Pensaste que unos besos arreglarían todo? No te engañes, Adara, tú sabes perfectamente que esa promesa no la puedes cumplir."
    
    hide i_ad_enojada
    show i_ad_frente at right
    nvl clear
    voice "N224.mp3"
    nvle "Helena se zafa de sus manos y se cruza de brazos frente a la rubia, la mira desafiante. Por su parte, Adara se ha quedado pasmada por las palabras tan filosas que le ha lanzado la castaña."
    voice "Adara_105.mp3"
    ad "Entiendo que falta resolver eso, pero no me quieras cambiar el tema ahora. Estamos hablando de qué vamos a hacer."
    he "Tú cambiaste el tema primero. Okay, va, es peligroso, incluso estúpido, seguir creyendo que podemos encarar a esa gente, pero ¿qué hago? ¿Regresar contigo como si nada hubiera pasado, como si todo aquello que me causaste se puede ignorar?"
    he "¿Hacemos eso? ¿Ignorar lo que pasó con mi mamá? Ni siquiera sé si en verdad está muerta, porque esa no era su carne. ¿O acaso entendí mal? Dime, te escucho. ¿Qué hacemos?"
    voice "Adara_106.mp3"
    ad "No, nada de eso. Lo de tu mamá es algo muy serio, pero lo que tuvimos también fue algo serio y yo no pienso volver a..."
    hide i_he_espalda
    show i_he_tres at leftdialogue
    nvl clear
    voice "N225.mp3"
    nvle "Del coraje repentino que le causan las palabras de Adara, Helena levanta los brazos mientras la encara con los ojos muy abiertos y la mandíbula apretada. Respira hondo y baja firme sus brazos en puños."
    he "¿Qué esta vez sí es en serio? ¡¿SÍ ES EN SERIO?! Adara, ¡me rompiste el corazón esa vez! No sólo me ilusionaste y luego dejaste que la realidad me azotara en la cara con tus crueles palabras, sino que además me humillaste."
    he "¿Sabes cuánto tiempo me tomó sanar? ¡¿Eh?!"
    voice "Adara_107.mp3"
    ad "No, por favor escúchame. Tú no me estás entendiendo. Sé que en el pasado te lastimé y-"
    he "Me hiciste creer que sentíamos lo mismo. Que queríamos lo mismo. ¿Y qué pasó el día que traté de dar un paso adelante?"
    nvl clear
    voice "N201.mp3"
    nvle "La postura de pelea de Helena se rompe por el nudo en la garganta que se forma seguido de las lágrimas que inundan sus ojos. Se agacha ligeramente y se tapa la cara para ahogar su llanto."
    voice "Adara_108.mp3"
    ad "Lo siento, yo no..."
    nvl clear
    voice "N201.mp3"
    nvle "Destapa de un lado su cara destrozada de dolor, sólo para apuntarle con un dedo de manera acusatoria, su cara se contrae de dolor y se da la vuelta ignorando a Adara. Esta por su parte se intenta acercar más a la castaña, pero le levanta la mano a modo de detenerla. Adara ve su mano y agacha la cabeza derrotada."

    voice "Adara_109.mp3"
    ad "Lena... no sé qué decirte para que me perdones, pero quiero que sepas que esa vez..."
    he "¡BASTA!"
    nvl clear
    voice "N201.mp3"
    nvle "Helena se aleja tapándose los oídos, Adara se acerca lentamente hasta quedar de rodillas a su lado."
    voice "Adara_110.mp3"
    ad "Fui una tonta, lo admito. No estaba lista y cuando tú lo estuviste no supe qué hacer, reaccioné de la peor manera... Lo siento, herí tus sentimientos y me siento terrible por ello."
    
    if caminoa_flag:
        hide i_he_tres
        show i_he_espalda at leftdialogue
        he "¡Já! Como si eso me importara ahora. Métete esto en la cabeza, Adara, esa labia tuya ya no tendrá efecto en mí. Yo ya no siento NADA, ni por ti ni por NADA."
    
    if caminob_flag:
        hide i_he_tres
        show i_he_espalda at leftdialogue
        he "¿Ah sí? Pues qué mal. A mí tu disculpa ya no me sirve de nada, ya no soy la misma ingenua que se desvivía por ti y tus mentiras."
    
    nvl clear
    voice "N201.mp3"
    nvle "Adara se acerca a Helena y esta la empuja dándole la espalda, desolada se abraza a sí misma encogiéndose un poco. Adara se muestra dolida ante la actitud de Helena."
    voice "Adara_111.mp3"
    ad "¿Hubieras preferido que nos mataran? ¿De verdad? Quiero escucharte decirlo, dime si no, Lena, ¿acaso no querías huir? Anoche nos juramos un futuro juntas, eso de 'No me voy a ir a ningún lado' ¿era mentira?"
    
    if caminoa_flag:
        hide i_he_espalda
        show i_he_tres at leftdialogue
        hide i_ad_frente
        show i_ad_tres at right
        he "Cállate, déjame en paz. ¿No me escuchaste? Ya no quiero estar contigo como lo quise antes."
        voice "Adara_112.mp3"
        ad "Helena, ¡ya basta! Ni me escuchas ni sales de tu hoyo. Estoy tratando de hacerte entender que he cambiado, que ahora sí haré bien las cosas contigo. Por favor, entiéndeme, Lena."
    
    if caminob_flag:
        hide i_he_espalda
        show i_he_tres at leftdialogue
        hide i_ad_frente
        show i_ad_tres at right
        he "¡No! Basta, Adara, cállate ya. No se trata de eso."
        voice "Adara_113.mp3"
        ad "Pues yo tampoco soy la misma. Poco me importa lo que se llegue a decir. Yo no bromeaba cuando te dije que iría a cualquier parte contigo. ¡Lena, entiéndeme, puta madre!"
    
    #TRACK 3 Lesbies
    play sound "track 3_lesbiesFinalMix.wav"


    ###### Escena ###############################
    #################################################
    scene bg adara casa with dissolve
    nvl clear
    voice "N201.mp3"
    nvle "Helena se queda sorprendida ante la declaración de Adara, se quedan mirando sin palabras, la rubia pega su frente a la de ella y sus alientos empiezan a combinarse. La castaña la mira detenidamente, Adara está impaciente, pero a la vez teme la respuesta de Helena y aleja su rostro para seguirla viendo, ve sus labios y luego sus ojos."
    
    scene bg aca with fade1
    if caminoa_flag:
        he "¿Qué me ves?"
        voice "Adara_114.mp3"
        ad "No te estoy viendo."

    if caminob_flag:
        he "¿Qué estás haciendo?"
        voice "Adara_115.mp3"
        ad "¿Qué estoy haciendo?"

    scene bg manos sex
    nvl clear
    he "Adara..."
    voice "Adara_116.mp3"
    ad "¿Sí?"
    he "Ara."
    voice "Adara_117.mp3"
    ad "Lena."

    scene bg sex uno
    nvl clear
    voice "N201.mp3"
    nvle "Adara suelta las muñecas de Helena y se queda con los brazos recargados sobre la pared entre la castaña, Helena por su parte baja sus brazos y toma a Adara por la cadera, la acerca firme hacia ella."

    if caminoa_flag:
        he "Esta es tu última oportunidad, arruínala y no vuelves a saber de mí."

    if caminob_flag:
        he "Te puedo dar una última oportunidad."

    scene bg sex 
    # TRACK 2 Lesbianismo
    play sound "LesbianismoTrack 2.mp3"

    nvl clear
    voice "N201.mp3"
    nvle "Las manos de Helena viajan por la espalda Adara y luego suben hasta sus hombros solo para bajar sus tirantes, mostrando así el top ajustado que cubre su busto. Helena entonces lleva sus manos acariciando la suave piel del cuello de la rubia hasta llegar a su mandíbula y mejillas, con ambas manos sostiene su cara y con fuerza la jala hacia la altura de su ojos haciendo que Adara pierda un poco su compostura."

    he "¿Entendiste?"
    voice "Adara_118.mp3"
    ad "Entendí, guapa."
    nvl clear
    voice "N201.mp3"
    nvle "Helena sonríe de manera satisfactoria y le da un beso, Adara le responde intensificando más el beso. Helena lleva sus manos hacia el cabello de Adara y lentamente le va deshaciendo sus trenzas liberando así la larga y ondulada cabellera de la rubia. Adara detiene un poco el beso, mira con lujuria a Helena y desliza sus manos hasta llegar a sus glúteos."

    voice "Adara_119.mp3"
    ad "¿Puedo?"
    nvl clear
    voice "N222.mp3"
    nvle "Helena asiente mordiéndose el labio inferior, Adara la carga y ella reacciona prontamente enganchando firmemente sus piernas a la cintura de la rubia. Adara sube a Helena cargando hacia la habitación mientras traza un camino de suaves besos por el cuello de Helena. Helena se sobresalta y se empieza a reír nerviosamente. Al llegar arriba Helena suelta un gemido y Adara cierra la puerta detrás de ellas."
    
    
    ###### Se van lejos ###############################
    #################################################
    scene bg cama with fade1
    nvl clear
    voice "N223.mp3"
    nvle "Helena se despierta por la luz de la luna que baña la cama de Adara, el cabello de la rubia parecen ondas de oro dispersos en su brazo y almohadas, su respiración es tan tranquila que a Helena le da miedo moverse del brazo de Adara para evitar interrumpir su paz. "
    voice "N224.mp3"
    nvle "Admira sus largas pestañas, sus labios carnosos, el subir y bajar de su pecho. Helena se levanta de la cama y se pone su ropa, junta sus cosas, yéndose."
    
    voice "Adara_120.mp3"
    ad "Y yo aquí esperando que me despertaras con un beso, esto es lo que recibo por esperar aquí quieta."
    he "¿Qué ya no tienes prisa por huir? Ayer te preocupaba mucho."
    nvl clear
    voice "N225.mp3"
    nvle "Helena se ríe de nervios y se tapa la cara al ver que la rubia siempre estuvo despierta."
    he "Me tienes a mí ahora, ¿de qué te quejas? ¿O qué, mi amor no es suficiente para ti?"
    voice "Adara_121.mp3"
    ad "Tu amor es algo que no merezco, pero que cuidaré el tiempo que tú me permitas. Me alegro que después de tanto tiempo, por fin puedo decirte que te amo, Lena."
    he "Te amo."

    scene bg adara casa with dissolve
    nvl clear
    show i_ad_tres at right with easeinright
    
    voice "Adara_122.mp3"
    ad "No puedo creer que esto sea real, han pasado tantas cosas estos últimos días. Lena, no me estoy equivocando esta vez ¿verdad? Yo te amo y tú lo sabes ¿verdad?"
    nvl clear
    voice "N226.mp3"
    nvle "Adara se levanta con ojos aguados. Tiene una expresión un tanto angustiada."
    show i_he_tres at leftdialogue with easeinleft
    if caminoa_flag:
        he "Ay, Ara, de las cosas que te terminas preocupando. ¿Apenas ahorita te detuviste a pensar en eso?"
    
    if caminob_flag:
        he "Yo también te amo, Ara. No te preocupes del pasado ni del futuro, sólo disfruta conmigo lo que tenemos ahora."
    
    nvl clear
    voice "N227.mp3"
    nvle "Helena toma la cara de Adara entre sus manos y le da un suave y dulce beso. Ambas chicas ríen por lo bajo."
    he "¿Quedó claro? Es más, te lo repito: Adara, te amo."
    nvl clear
    voice "N228.mp3"
    nvle "Helena toma una de las flores de caléndula que quedaron aplastadas por la van el día anterior, la admira con ojos tristes y una tierna sonrisa y la huele."
    voice "Adara_123.mp3"
    ad "¿Estás lista, Lena?"

    ##### Decisión
    menu:
        "Mmmm me pregunto lo mismo.":
            he "Mmmm me pregunto lo mismo."

        "Sip, vamos.":
            he "Sip, vamos."

    nvl clear
    voice "N229.mp3"
    nvle "Adara le extiende su mano a Helena, esta toma su mano y se levanta del suelo."
    he "Ara, ¿tendrás un libro que me regales?"
    voice "Adara_124.mp3"
    ad "Claro, amor, ¿qué libro te gustaría?"
    he "El que sea, es para esta flor de caléndula, la recogí antes de que se llevaran a Chancho. Llevaré una conmigo para siempre traer algo que me recuerde a mi madre y a Chancho."
    voice "Adara_125.mp3"
    ad "Te daré mi diario para que también me recuerdes a mí."
    nvl clear
    voice "N230.mp3"
    nvle "La pequeña flor queda prensada entre las hojas del diario de Adara, Helena guarda el diario de cuero en uno de sus bolsillos internos de la sudadera, ahora es ella la que le extiende la mano a Adara, la rubia acepta el gesto entrelazando su mano con la de ella y equipadas con sus mochilas se van caminando hacia el alba."
    
    
    ###### FINAL 3 NOVIAS ###########################
    #################################################
    
    $ final_arbol = True
    scene black with slow_dissolve
    show screen arbol_screen with fade2
    ""
    ""
    ""
    ""
    return

## RUTA SECUESTRO ###################################
label secuestro:
    
    $ ui_secuestro = True
    $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)
    hide screen arbol_screen
    $ principal_flag = False
    $ novias_flag = False
    $ coqueteo_flag = False
    $ flash_flag = False
    $ secuestro_flag = True
    $ salvar_flag = False
    $ caminoa_flag = False
    $ caminob_flag = False


    ###### Secuestro Enterrar #######################
    #################################################
    scene bg bosque
    nvl clear
    nvle "Helena entierra la caja. Su llanto se calma. El viento se lleva las últimas lágrimas."
    show i_he_tres at leftdialogue
    show i_ad_tres at right
    voice "Adara_126.mp3"
    ad "¿Segura que vas a estar bien con esto?"

    ##### Decisión 
    menu:
        "Tengo que estar bien, voy a estar bien.":
            he "Tengo que estar bien, voy a estar bien."
            voice "Adara_127.mp3"
            ad "Aquí estaré para apoyarte, Lena."
            ad "Somos amigas a final de cuentas."
            he "Perdón, sé que he sido un poco grosera contigo."
            voice "Adara_128.mp3"
            ad "Pero no lo has sido."

        "La verdad, no lo sé, me da algo de miedo.":
            voice "Helena_145.mp3"
            he "La verdad, no lo sé, me da algo de miedo."
            voice "Adara_120.mp3"
            ad "Está bien tener miedo."
            voice "Helena_146.mp3"
            he "Es que no entiendo, ¿qué hicimos mal? ¿qué hice mal? ¿por qué sucedió todo esto?"
    
    voice "Helena_147.mp3"
    he "Me pregunto cómo llegamos hasta aquí."
    
    voice "Adara_130.mp3"
    ad "No lo sé, tal vez la noche nos lo diga."
    nvl clear
    nvle "Adara está sentada en el sofá tomando un café. Helena, se sienta a la mesa. Chancho las observa."

    voice "Helena_148.mp3"
    he "Ya lo pensé y... creo que debo irme de la ciudad."
    voice "Adara_131.mp3"
    ad "Vele el lado bueno, no sería la primera vez que huyes je...je..."
    nvl clear
    nvle "Helena sacude la cabeza a manera de desaprobación mientras se ríe. Mira a lo lejos un momento, se queda de brazos cruzados y suspira al voltear con Adara."

    voice "Helena_149.mp3"
    he "¿Te quedarías a Chancho si me voy?"
    voice "Adara_132.mp3"
    ad "¿No sería mejor irnos todos y ya?"

    ##### Decisión 
    menu:
        "¿En serio quieres ir conmigo?":
            voice "Helena_150.mp3"
            he "¿En serio quieres ir conmigo?"

        "No, Adara, entiende.":
            voice "Helena_151.mp3"
            he "No, Adara, entiende, debo irme sola."

    scene bg magenta helenadara with dissolve
    
    voice "Adara_133.mp3"
    ad "Te he estado esperando todo este tiempo. Déjame ir contigo."
    voice "Helena_152.mp3"
    he "Pero y... ¿a dónde iríamos?"
    voice "Adara_134.mp3"
    ad "No lo sé, Lena, hasta donde no recordemos lo que hemos pasado."
    scene bg noche
    nvl clear
    nvle "Adara le extiende su mano a Helena, y esta baja sus brazos, antes cruzados, para tomar la mano de Adara entre las suyas y ponerla contra su mejilla. Cierra los ojos al contacto del calor de su palma y Adara se acerca un poco más hacia Helena."
    voice "Helena_153.mp3"
    he "Que sea más lejos."

    scene bg calle
    nvl clear
    nvle "Adara le sonríe a Helena y termina poniendo su otra mano en el rostro de la joven haciendo que esta la voltee a ver con con el ceño fruncido, pero con cariño saliendo de sus ojos. Sus cuerpos se aproximan los unos a los otros."
    scene bg casa with fade2
    nvl clear
    nvle "Sus rostros siguen el mismo camino, Helena suelta la mano de Adara sin darse cuenta al quedar prendada de su mirada, se ruboriza y cierra los ojos con nerviosismo. Adara le responde con un cálido abrazo, pero Helena abre los ojos con una ligera mueca de dolor; le regresa el abrazo a la rubia y oculta su cara en su hombro."
    nvle "La casa está en silencio. Helena duerme en el sillón, envuelta en una manta. Chancho está a sus pies, hecho bolita. Adara ronca leve desde un sillón opuesto."
    show i_he_tres at leftdialogue
    show i_ad_tres at right
    voice "Helena_154.mp3"
    he "¿Qué fue eso...?"
    nvl clear
    nvle "Otro ruido. Esta vez, más cerca."
    ch " Oink..."
    nvl clear
    nvle "Helena camina hacia la puerta. La abre lentamente. Nada. Silencio. Y de pronto..."
    hide i_he_tres
    hide i_ad_tres
    show secuaz aguila at left
    ""
    show secuaz oso at right
    nvl clear
    nvle "Híbridos entran a toda velocidad. Un gas se dispersa. Chancho grita. Adara salta de su lugar."
    show secuaz jaguar at leftdialogue
    voice "Helena_155.mp3"
    he "¡No, no, no!"
    show secuaz tlacuache at centerup
    nvl clear
    nvle "Todo se vuelve confuso. Manos que sujetan. Gas que ahoga. Golpes secos. Voces apagadas."


    ###### Secuaces de Elodia #######################
    #################################################
    scene bg laboratorio with fade2
    nvl clear
    voice "N242.mp3"
    nvle "Helena despierta desorientada. Se levanta con dificultad."
    voice "N243.mp3"
    nvle "La puerta se abre y entra la Dra. Elodia Rivas."
    show elodia at centerup
    voice "N244.mp3"
    nvle "Su porte es calmo, su voz firme. Lleva su bata impecable, una carpeta en la mano."
    

    ###### Laboratorio Secuestro #########################
    #################################################
    hide elodia
    show i_el_tres at rightup with easeinright
    el "Buenos días, Helena." 
    show i_he_enojo at leftdialogue 
    voice "Helena_156.mp3"
    he "¡¿Dónde estoy?! ¡¿Dónde está Chancho?! ¡¿Dónde está Adara?!"
    nvl clear
    voice "N245.mp3"
    nvle "Elodia cierra la puerta con suavidad. Deja la carpeta sobre la mesa. La observa un momento."
    voice "Helodia_13.mp3"
    el "Todos están vivos. A salvo. Por ahora."
    voice "Helena_157.mp3"
    he "¡¿Qué es este lugar?! ¡¿Quién eres?!"
    voice "Helodia_14.mp3"
    el "Soy la Dra. Elodia Rivas. Tal vez has oído hablar de mí... aunque seguramente no como deberías."
    nvl clear
    voice "N246.mp3"
    nvle "Helena da un paso atrás. Su rostro se crispa de furia y confusión."
    voice "Helena_158.mp3"
    he "¡Tú...! ¡Fuiste tú!"
    show mamaCatrePantalla with fade2
    nvl clear
    voice "N247.mp3"
    nvle "Baja una pantalla del techo, se enciende y muestra a su madre"
    voice "Helodia_15.mp3"
    el "Sí. Pero no fue un acto de crueldad. Fue necesidad. Tu madre tomó algo. Protegía a alguien muy importante. Y eso... podía cambiarlo todo."
    voice "Helena_159.mp3"
    he "¡La encerraste como a un animal! ¡La convertiste en uno!"
    play sound "Helodia_16.mp3"
    el "Yo no, el virus lo hizo."
    hide mamaCatrePantalla with fade3
    el "Tu madre es fuerte. Pero no pudo evitarlo. Nadie puede, cuando el virus se arraiga el cuerpo es afectado, pero su conciencia... resistió."

    voice "Helena_160.mp3"
    he "¿Por qué lo hiciste? ¿Dónde está Adara?"
    hide i_el_tres 
    show i_el_frente at right with dissolve
    voice "Helodia_17.mp3"
    el "Adara está bien, ella tiene un propósito aquí, así como tú."
    nvl clear
    voice "N248.mp3"
    nvle "Elodia abre la carpeta. Fotografías de Helena, informes, datos biométricos. Una imagen de su cerebro resaltado en rojo."
    
    scene bg amarillo elodia with fade3
    nvl clear
    voice "Helodia_18.mp3"
    el "Tu conciencia es distinta. Es como... una red. Estás hecha para sobrevivir a la mutación sin perderte. Eres una pieza perdida de esta evolución."
    voice "Helena_161.mp3"
    he "¡Oh, claro! ¡Y ahora quieres que me una a tu secta de monstruos conscientes!"
    play sound "Helodia_19.mp3"
    el "No monstruos. Humanos, que entendieron que el cuerpo es efímero. Que lo único que vale la pena preservar es la conciencia. La autopercepción. La memoria. La capacidad de reconocer al otro."
    el "¿Qué somos sin eso, Helena? Solo carne. Solo miedo."
    scene bg laboratorio
    nvl clear
    show i_el_frente at center 
    nvl clear
    voice "N249.mp3"
    nvle "Helena se queda en silencio. La voz de Elodia es suave, pero cortante como un bisturí."
    voice "Helodia_20.mp3"
    el "Tú puedes ayudarme. A salvar a los que están atrapados entre la mutación y el olvido. A tu madre. A Chancho. A Adara."
    hide i_el_frente with dissolve
    show i_el_frente at right with dissolve
    show i_he_enojo at left
    voice "Helena_162.mp3"
    he "¡No los toques!"
    voice "Helodia_21.mp3"
    el "Ya lo hice. Pero juntas podemos deshacer lo que otros empezaron."
    el "Solo si trabajas conmigo. Si decides mirar más allá del asco, del miedo, y ves lo que podría ser el futuro."
    nvl clear
    voice "N250.mp3"
    nvle "Silencio. Helena tiembla."
    voice "Helena_163.mp3"
    he "No pienso trabajar contigo."
    voice "Helodia_22.mp3"
    el "Entonces se acaban las opciones. Y será tu elección que los pierdas."
    voice "Helodia_23.mp3"
    scene bg amarillo elodia with fade2
    nvl clear
    el "¿Qué dices Helena?"

    ##### Trabajo ###################################
    menu: 
        
        "Jamás.":
            scene bg laboratorio 
            show i_he_enojo at leftdialogue with dissolve
            voice "Helena_164.mp3"
            he "Jamás."
            jump contexto

        "...salvaré a mi mamá":
            scene bg laboratorio 
            show i_he_enojo at leftdialogue with dissolve
            voice "Helena_166.mp3"
            he "Trabajaré contigo y salvaré a mi mamá"
            show i_el_tres at rightdialogue with dissolve
            voice "Helodia_24.mp3"
            el "Perfecto, no te arrepentirás."
            #Jump porque no vuelvo
    ###### TRABAJO
 

    ###### Contexto virus ###########################
    #################################################
    label ElodiaUI_label:
        $ ui_contexto = True
        $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)
        hide screen arbol_screen
        $ principal_flag = False
        $ novias_flag = False
        $ coqueteo_flag = False
        $ flash_flag = False
        $ secuestro_flag = True
        $ salvar_flag = False
        $ caminoa_flag = False
        $ caminob_flag = False
        
    scene bg laboratorio
    nvl clear
    
    voice "N251.mp3"
    nvle "Helena camina en silencio por el corredor aséptico del laboratorio."
    voice "N252.mp3"
    nvle "A su lado, la Dra. Elodia Rivas la guía con paso firme, sosteniendo una tableta con registros."
    voice "N253.mp3"
    nvle "Pasillos estrechos, iluminados con frialdad. Vidrios gruesos a los costados muestran otras salas: contenedores sellados, escritorios con monitores encendidos, tanques de oxígeno, cajas con etiquetas codificadas."
    voice "N254.mp3"
    nvle "Se detienen frente a una máquina refrigerada. Elodia abre un compartimento sellado y saca una pequeña bandeja de metal."
    voice "N255.mp3"
    nvle "En el centro: un cubo de carne cruda, pequeño, jugoso, pálido."
    
    show i_el_tress at leftdialogue with moveinright
    voice "Helodia_25.mp3"
    el "Sujeto de prueba 64F. Edad treinta y siete. Conciencia previa estable, etapa de transición incompleta. Método de preservación: criogenía interrumpida."
    nvl clear
    voice "N256.mp3"
    nvle "Le entrega el cubo a Helena en una pinza."
    voice "Helodia_26.mp3"
    el "Si ves algo, cualquier cosa... necesito que lo describas tal cual."
    show pruebaCarne
    nvl clear
    voice "N257.mp3"
    nvle "Helena toma el cubo con recelo. Finalmente, lo lleva a la boca y lo muerde. Masticación lenta. Traga."
    voice "N258.mp3"
    nvle "De inmediato, sus pupilas se dilatan."
    show almas with fade1
    voice "N259.mp3"
    nvle "Vemos a través de su mente: una habitación cerrada. Una mujer de cabello canoso y mirada extraviada. Cuerpo fracturado."
    voice "xim1.ogg"
    ma "Yo aún estoy aquí... yo... ¡yo soy!"

    scene bg laboratorio with fade2
    nvl clear
    show helena crisis with dissolve
    voice "N260.mp3"
    nvle "De golpe, la visión se apaga. Helena jadea y cae de rodillas, pero se repone rápido."
    hide helena crisis
    show i_he_tress at rightdialogue with dissolve
    voice "Helena_167.mp3"
    he "Fragmentado... pero resistía. No completamente ida."
    show i_el_tress at leftdialogue with dissolve
    voice "Helodia_27.mp3"
    el "Interesante. Anótalo."
    nvl clear
    voice "N261.mp3"
    nvle "Se lo dice a una grabadora de solapa en su bata."

    scene bg amarillo helena with fade2
    nvl clear
    voice "Helena_168.mp3"
    he "¿Será esto real? ¿Será una visión más? ¿Una visión de mí misma?"

    scene bg laboratorio with fade3
    show i_he_tress at rightdialogue with dissolve
    voice "Helena_169.mp3"
    he "Elodia, tengo algo que decirte."

    ##### Decisión
    menu:
        "A veces confundo la realidad con visiones.":
            voice "Helena_170.mp3"
            he "A veces confundo la realidad con visiones."

        "No sé si quiero seguir...":
            voice "Helena_171.mp3"
            he "No sé si quiero seguir haciendo esto."

    show i_el_tress at leftdialogue with dissolve
    el "¿Cómo?"
    voice "Helena_172.mp3"
    he "A veces no sé si esto es real... Es como si todo el tiempo acabara de comer carne."
    voice "Helodia_28.mp3"
    el "La mente suele protegerse distorsionando lo imposible. Pero esto, Helena, es tan real como el cuerpo que habitas."
    voice "Helena_173.mp3"
    he "Es que no me gusta y no sé si en verdad estamos haciendo un avance."
    voice "Helodia_209.mp3"
    el "¡Claro que estamos avanzando! Que no veamos los resultados inmediatamente no significa que no los haya."
    el "¿Te vas a rendir con tu mamá, acaso?"
    voice "Helena_174.mp3"
    he "No, no, sigamos."


    ###### Trabaja con Elodia #######################
    #################################################
    scene bg jeringa with fade3
    nvl clear
    voice "N262.mp3"
    nvle "Helena está sentada en una silla metálica."
    voice "N263.mp3"
    nvle "Un brazo desnudo reposa sobre un apoyabrazos acolchado. A su alrededor, pantallas y bandejas con tubos de ensayo. Elodia prepara una jeringa."

    voice "Helodia_30.mp3"
    el "Esto no dolerá mucho."
    
    ##### Decisión
    menu:
        "Eso dijiste la última vez.":
            voice "Helena_175.mp3"
            he "Eso dijiste la última vez."

        "Ya estoy acostumbrada a que todo me duela.":
            voice "Helena_176.mp3"
            he "Ya estoy acostumbrada a que todo me duela."

    nvl clear        
    voice "N264.mp3"
    nvle "La aguja entra. La sangre fluye, oscura, densa."

    scene bg laboratorio piso
    nvl clear
    show i_he_lateral at left with dissolve
    voice "Helena_177.mp3"
    he "¿Crees que si tengo esta habilidad... también tengo el virus?"
    nvl clear
    voice "N265.mp3"
    nvle "Elodia mira el tubo llenándose."

    show i_el_frente at rightup with dissolve
    voice "Helodia_31.mp3"
    el "Tal vez. El virus fue creado para adaptarse a cualquier entorno imitando capacidades animales: regeneración, resistencia, detección de vibraciones, hibernación... habilidades para sobrevivir al fin del mundo que se avecinaba."
    el "Pero lo tuyo... ver recuerdos a través de la carne... eso no existe en el reino animal."
    hide i_el_frente
    hide i_he_lateral
    show helena bata at rightdown with dissolve
    voice "Helena_178.mp3" 
    he "Entonces, ¿qué soy? ¿Un híbrido?"
    show elodia tress at leftdialogue with dissolve
    voice "Helodia_32.mp3"
    el "Una anomalía. Algo nuevo. Algo que no debió existir, y sin embargo... estás aquí."
    scene bg jeringa with fade3
    nvl clear
    voice "N266.mp3"
    nvle "La jeringa se llena. Elodia la retira y coloca el tubo con cuidado en una bandeja sellada."
    voice "Helodia_33.mp3"
    el "Y eso, Helena, es más fascinante que cualquier plan original. Porque la verdadera evolución... nunca es la prevista.{p=1.5}Por eso eres importante."


    ###### Entrega a Chancho ########################
    #################################################
    scene bg laboratorio with fade3
    nvl clear
    voice "N267.mp3"
    nvle "Elodia y Helena caminan juntas en silencio. Elodia se detiene frente a una bifurcación. Mira a Helena. "
    show i_el_frente at leftdialogue with dissolve
    voice "Helodia_34.mp3"
    el "Helena... necesito pedirte algo más."
    nvl clear
    voice "N268.mp3"
    nvle "Helena se queda quieta. Ya sabe ese tono. Esa pausa. Ese algo más nunca es leve."
    voice "Helodia_35.mp3"
    el "Tu amigo. Chancho."

    hide i_el_frente
    show i_he_bgrande at right with dissolve
    show i_el_tres at leftdialogue with dissolve

    ##### Decisión
    menu:
        "Pensé que Chancho no te servía.":
            voice "Helena_179.mp3"
            he "Pensé que Chancho no te servía."

        "Chancho alegra mis días aquí.":
            voice "Helena_180.mp3"
            he "Chancho alegra mis días aquí."

    voice "Helodia_36.mp3"
    el "Chancho podría ser la pieza fundamental. Su existencia podría reescribir todo lo que sabemos sobre transmisión de conciencia. No quiero destruirlo. Quiero entenderlo. Preservarlo."
    voice "Helena_181.mp3"
    he "Él no confía en nadie. Apenas y se deja tocar por mí."
    voice "Helodia_37.mp3"
    el "Es una anomalía. Una joya de mutación espontánea. De animal a humano. Eso no estaba previsto en el virus MA."
    nvl clear
    voice "N268.mp3"
    nvle "Helena no responde. El silencio es un campo minado."
    voice "Helodia_38.mp3"
    el "Necesito hacer pruebas con él. Solo observación clínica. Lecturas. No lo lastimaré."
    nvl clear
    voice "N270.mp3"
    nvle "Helena frunce el ceño. Sus dedos juegan con el dobladillo de la bata."
    voice "Helodia_39.mp3"
    el "No lo forzaré. Pero si tú se lo pides..."

    ##### Decisión
    menu:
        "Pero déjame ver a Adara.":
            voice "Helena_182.mp3"
            he "Pero déjame ver a Adara."
            scene bg elodia helena with fade3
            nvl clear
            voice "Helodia_40.mp3"
            el "Helena, Adara ya no está aquí."
            voice "Helena_183.mp3"
            he "¿Cómo?"
            voice "Helodia_41.mp3"
            el "La dejé ir, ella no me sirve."
            voice "Helodia_42.mp3"
            el "Déjame observar a Chancho, no le haré nada."

        "No quiero que experimentes con Chancho.":
            voice "Helena_184.mp3"
            he "No quiero que experimentes con Chancho."
            voice "Helodia_43.mp3"
            el "Helena, no vamos a avanzar si no lo observamos."
            scene bg elodia helena with fade3
            nvl clear
    
    nvl clear
    voice "N271.mp3"
    nvle "Finalmente, asiente. Una vez. Breve."
    scene bg laboratorio piso
    nvl clear
    show chancho parado sec at rightdown
    ch "Oink... "
    nvl clear
    nvle "Chancho entra con pasos dudosos. Mira todo. Luego ve a Elodia. Se queda junto a la puerta."
    nvle "En el piso hay dos círculos, uno verde y uno rojo."

    el "Hola cerdito. Si me entiendes puedes pararte en el círculo verde."
    nvl clear
    nvle "Elodia se agacha a la altura del cerdo."
    el "¿Sabes quién eres?"
    ch "Oink..."
    el "Si eres un cerdo párate en el círculo verde."
    hide chancho parado sec 
    show chancho desnudo sentado sec at rightdown 
    nvl clear
    nvle "Chancho se rasca la cabeza. Se sienta en la alfombra ignorando a Elodia."
    nvle "Elodia, en un cuarto contiguo, observa desde una ventana de cristal unidireccional. Se frustra."


    ###### Nueva celda ##############################
    #################################################
    show mamaCatrePantalla with fade2
    nvl clear
    nvle "La puerta se cierra automáticamente a su espalda. Helena se acerca a la pantalla. Se enciende con un leve parpadeo."
    nvle "En ella, hay una toma de vigilancia. Su madre."
    nvle "Hortensia está sentada en una silla, frente a una pared blanca. Su cabello está recogido de forma torpe. Tiene vendajes en los brazos, pero está despierta. Se balancea suavemente. Tararea algo muy bajito."
    nvle "Helena no parpadea. No dice nada. Se queda mirando durante un largo rato. Observa cada gesto, cada movimiento leve de los dedos de su madre."
    nvle "La pantalla no tiene sonido. Solo silencio."

    nvle "Finalmente, Helena se gira. Camina hacia la cama. Se recuesta boca arriba, con los brazos cruzados sobre el pecho. Mira al techo. Sus ojos no parpadean. La respiración es pesada, pero estable."
    voice "Helena_185.mp3"
    he "Te voy a sacar de ahí..."

    scene bg lab with fade1
    nvl clear
    nvle "Helena está sentada en la misma silla de siempre. Brazo extendido. Elodia prepara una nueva jeringa. Sus movimientos son suaves, médicos, casi mecánicos."
    nvle "Helena la observa con el ceño fruncido. Tiene ojeras, el cabello más desordenado que de costumbre."
    
    show i_he_sec at leftdialogue with dissolve
    voice "Helena_186.mp3"
    he "Ya pasó mucho tiempo. No me has dicho nada de Chancho."
    nvl clear
    nvle "Elodia no responde. Se limita a colocar el torniquete y preparar la aguja."
    voice "Helena_187.mp3"
    he "¡Elodia!"
    show i_el_tres at rightdialogue with easeinright
    voice "Helodia_44.mp3"
    el "Te dije que las pruebas tomarían tiempo."
    voice "Helena_188.mp3"
    he "No me dijiste que me lo ibas a quitar."
    voice "Helodia_45.mp3"
    el "Estamos muy cerca."

    scene bg amarillo elodia with fade3
    nvl clear
    voice "Helodia_46.mp3"
    el "El virus Metamorfosis Adaptativa hubiera podido ser una joya maldita. Un diseño perfecto, liberado por desesperados."
    play sound "Helodia_47.mp3"
    el "Su objetivo era noble: supervivencia. Climas extremos, hambrunas, toxicidad ambiental... Era la siguiente etapa de la humanidad."
    hide bg amarillo elodia
    el "Pero no supieron esperar. Lo soltaron incompleto. Y mira dónde estamos ahora."

    nvl clear
    nvle "Pausa."
    scene bg hongos
    nvl clear
    voice "Helodia_48.mp3"
    el "De casualidad... ¿comes muchos hongos?"
    nvl clear
    nvle "Helena parpadea, desconcertada."

    ##### Decisión
    menu:
        "Soy... era... vegana.":
            voice "Helena_189.mp3"
            he "Soy... era... vegana."
            voice "Helena_190.mp3"
            he "A veces comía setas del bosque. Mi madre me enseñó."

        "No desde que estoy aquí.":
            voice "Helena_191.mp3"
            he "No desde que estoy aquí."

    scene bg verde with dissolve
    
    show i_el_tres at rightdialogue with easeinright
    voice "Helodia_49.mp3"
    el "Estamos investigando si el virus puede adaptarse al reino fungi... Puede que hayamos encontrado algo."
    show i_he_sec at leftdialogue with dissolve
    voice "Helena_192.mp3"
    he "¿El virus MA en hongos?"
    el "No creo que podamos llegar a esas conclusiones todavía."

    scene bg lab with fade3
    nvl clear
    nvle "La luz está apagada. Helena está sentada en el piso junto a la cama. La pantalla donde suele ver a su madre está en negro. La habitación huele a humedad, encierro y desesperanza."
    nvle "Sus labios están agrietados. Sus brazos, marcados por pinchazos. Tiene bandejas con restos de carne sobre la mesa, todas medio llenas, apenas tocadas."

    show i_he_enojo at leftdialogue with dissolve
    voice "Helena_193.mp3"
    he "Estoy harta..."
    nvl clear
    nvle "Se levanta. Cruza la habitación. Golpea la puerta. Una, dos, tres veces."
    voice "Helena_194.mp3"
    he "¡AAAAAAAAAAAAH!"


    #TRACK 4 Laboratorio
    play sound "track 4_lab FinalMix.wav"

    scene bg laboratorio 
    nvl clear
    nvle "Helena está frente a Elodia. Las luces frías, el mismo ambiente clínico. Hay una bandeja cubierta frente a ella. Elodia la destapa. Un nuevo trozo de carne cruda, brillante y rosada."
    
    voice "Helodia_50.mp3"
    el "Adelante Helena. Este es uno de los sujetos más prometedores que hemos tenido."
    show pruebaCarne with fade3
    nvl clear
    nvle "Helena la mira largo rato. Finalmente, toma la carne. La lleva a la boca."
    nvle "Lo mastica. Traga. Y entonces..."
    #scene bg chancho lodo with fade2
    show chancho desnudo at right 
    ch "Lena... me gustaban las caléndulas."

    scene bg laboratorio with fade2
    nvl clear
    nvle "Helena se congela. Una lágrima baja por su mejilla. Su cuerpo comienza a temblar."
    play sound "audio/Foley/Bandeja cayendo.mp3"
    nvle "La bandeja cae al suelo. Se rompe en dos. "
    show i_he_enojo at leftdialogue with dissolve
    voice "Helena_195.mp3"
    he "No..."
    voice "Helena_196.mp3"
    he "¡ES ÉL! ¡ES CHANCHO!"
    scene bg rojo helena with fade3
    nvl clear
    nvle "Se lanza sobre Elodia. Grita, empuja, quiere morder, golpear. Elodia, le inyecta algo en el cuello. Helena se tambalea. Dos hombres entran corriendo."
    scene bg laboratorio
    nvl clear
    show secuaz aguila at left
    ""
    show secuaz oso at right
    ""
    show secuaz jaguar at leftdialogue
    voice "Helena_197.mp3"
    he "¡Tú lo mataste! ¡Lo mataste! ¡Eres una maldita...!"
    show secuaz tlacuache at centerup
    nvle "Los hombres la sujetan. Ella forcejea con una fuerza animal, pero ya está sedada. Es arrastrada por el pasillo."
    hide secuaz tlacuache
    show i_el_tres at rightdialogue with easeinright
    voice "Helodia_51.mp3"
    el " No lo entiendes ahora. Pero lo harás. Pronto."
    nvl clear
    nvle "La puerta de su habitación se cierra de golpe."

    scene bg lab with fade2
    nvl clear
    nvle "Una bandeja de comida fría se encuentra intacta junto a la puerta. Sobre ella, carne cruda en trozos pequeños."
    show helena esclava
    nvle "Helena está encorvada en una esquina, con las rodillas contra el pecho."
    show i_el_tress at leftdialogue with easeinleft
    nvle "La puerta se abre. Elodia entra. Luce impecable. Fría. Inmutable. Lleva una tableta entre los brazos y se detiene frente a ella, sin bajar la mirada."
    voice "Helodia_52.mp3"
    el "Necesitas alimentarte."
    nvl clear
    nvle "Helena no responde. Se limita a girar la cabeza hacia la pared."
    voice "Helodia_53.mp3"
    el "Sabes lo que estás rechazando, ¿no? El poder de ver. De recordar."
    voice "Helena_198.mp3"
    he "No quiero ver nada más."
    play sound "Helodia_54.mp3"
    el "Podríamos hacer historia juntas. Erradicar el miedo. Redefinir la humanidad."
    el "Pero prefieres pudrirte en este rincón, como si eso honrará algo. Como si esa resistencia fuera noble."
    stop sound
    voice "Helena_199.mp3"
    he "Prefiero pudrirme que convertirme en ti."
    nvl clear
    nvle "Elodia no reacciona. Sólo suspira."
    hide i_el_tress
    nvle "La habitación ha cambiado. Más fría. Sin cama. Sin pantalla. Sólo concreto, una cubeta, y un grillete en la pared. El metal está oxidado."
    nvle "Helena yace encadenada de un tobillo. El grillete le permite moverse sólo un metro y medio. No hay ventana. El aire huele a cloro y humedad."
    nvle "Días pasan. Sin voz. Sin luz natural. La carne sigue llegando. Y sigue pudriéndose."
  
    jump esclava


## Contexto Historia ################################
label contexto:
     
    ###### Contexto Historia ########################
    #################################################
    scene bg laboratorio
    nvl clear
    show i_he_enojo at leftdialogue with dissolve
    voice "Helena_165.mp3"
    he "Jamás. Nunca voy a trabajar contigo. Eres una estúpida si pensabas que iba a cooperar."
    show i_el_tres at rightup with easeinright
    nvle "Elodia no se inmuta. La mira como si se tratara de una niña obstinada, no de una amenaza."
    el "¿Y crees que tu madre sí quiso cooperar? ¿Que fue voluntaria? No, querida... Yo no trabajo con voluntarios. Trabajo con resultados."
    el "Obtengo todo lo que quiero. Siempre. Aunque me digan que no."
    nvl clear
    nvle "Elodia comienza a acercarse."
    scene bg magenta hortensia
    nvl clear
    el "Tu madre, durante su última entrega, le pedí que me ayudara a meter el encargo al depósito, no sospechó nada. Estaba tan preocupada por ayudar..."
    el "Tanta amabilidad. Tanta ingenuidad. Fue su perdición. Le inyecté un sedante. Cayó como una hoja seca."
    el "Ni siquiera luchó. Fue decepcionante."
    scene bg laboratorio with fade3
    nvl clear
    show i_he_sec at leftdialogue with dissolve
    show i_el_tres at rightup with easeinright
    nvl clear
    nvle "Helena estalla. Grita y se lanza contra ella, los ojos brillando de odio."
    he "¡Maldita seas! ¡Te voy a matar!"
    nvl clear
    nvle "Elodia no se altera. Toma una inyección de su bata. Esquiva el ataque de Helena y le inyecta."
    nvle "Helena cae de rodillas. Su respiración se vuelve pesada. Tiembla. Se desmorona."
    hide i_he_sec
    show secuaz tlacuache at left
    nvl clear
    nvle "La puerta se abre. Dos hombres entran. Uno la toma de los brazos, el otro de las piernas."
    show secuaz aguila at right
    el "Llévenla. Célula 64. Mantengan el régimen de ayuno por tres días. Luego... que coma."

    label pierde:

        ###### Pierde a Chancho #########################
        #################################################
        scene bg lab with fade3
        nvl clear
        show helena secuestro at leftdialogue
        nvle "Helena está encadenada de ambos pies. Su cabello está enmarañado, su piel pálida. No ha comido. Apenas ha dormido."
        nvle "La puerta se abre con un zumbido. Entra uno de los hombres. En las manos lleva una bandeja con un pedazo de carne."
        show secuaz oso at center
        voice "Secuaz2.mp3"
        s1  "Hora de comer."
        play sound "audio/Foley/Cadenas 1.mp3"
        if persistent.audio_cues:
        $ Descripcion = "Se escuchan cadenas"
        he "No quiero."
        show secuaz perro at right
        voice "Secuaz3.mp3"
        s2 "No es una opción."
        if persistent.audio_cues:
        $ Descripcion = ""
        nvl clear
        nvle "La agarra por el cabello. Le abre la boca a la fuerza y empuja el trozo de carne contra su lengua. Helena se retuerce, pero sus fuerzas son escasas. La carne entra. Traga."
        show almas with fade3
        nvle "El mundo se estira. La visión se distorsiona. Voces. Imágenes."
        #scene bg chancho lodo with fade1
        nvl clear
        show chancho desnudo at right
        show hortensia at leftdialogue
        nvle "Una granja. Hortensia. caléndulas. Chancho ven ya nos vamos. Helena despierta de golpe, escupiendo, confundida, entre vómito y lágrimas."
        scene bg lab with fade1
        nvl clear
        show helena secuestro at leftdialogue
        nvle "Elodia aparece detrás del sujeto sobre la puerta."
        show i_el_frente at right
        el "Tu conciencia sigue intacta. La red neuronal ha reaccionado. Tus memorias siguen sin colapsar."
        nvl clear
        nvle "Helena se congela. Mira la bandeja vacía. Tiembla."
        el "Él fue un buen espécimen. Resistente."
        hide i_el_frente
        nvl clear
        play sound "audio/Foley/Cadenas 2.mp3"
        nvle "Helena grita. Golpea la pared. Sus cadenas tintinean. Rompe en llanto."

    jump esclava
    
    
## FINAL 2 Esclava ##########################################
label esclava:
    $ ui_esclava = True
    label esclavaUI_label:
        $ config.mouse_displayable = MouseDisplayable("gui/handpointeruno.png", 15, 15)
        hide screen arbol_screen
        $ principal_flag = False
        $ novias_flag = False
        $ coqueteo_flag = False
        $ flash_flag = False
        $ secuestro_flag = True
        $ salvar_flag = False
        $ caminoa_flag = False
        $ caminob_flag = False


    ###### Conejillo de indias ######################
    #################################################
    scene bg lab with fade1
    nvl clear
    voice "N321.mp3"
    play sound "audio/Foley/Cadenas 3.mp3"
    if persistent.audio_cues:
        $ Descripcion = "Se escuchan cadenas"
    nvle "La puerta se abre. Helena está más flaca. Esta vez, dos hombres con uniforme entran. Le quitan la cadena del tobillo. La levantan con brusquedad."
    show helena esclava at center
    voice "Helena_200.mp3"
    he "¡Suéltenme!"
    nvl clear
    voice "N322.mp3"
    if persistent.audio_cues:
        $ Descripcion = ""
    nvle "La arrastran por el pasillo. Su cuerpo está débil, pero la rabia la mantiene en pie."
    voice "N323.mp3"
    nvle "La atan a una silla de metal. La iluminación directa le quema la vista. Frente a ella, una mesa con una bandeja tapada por un paño blanco."
    show i_el_tres at rightdialogue with easeinright
    voice "N324.mp3"
    nvle "Elodia entra."
    voice "Helodia_55.mp3"
    el "Hubo complicaciones. Tu madre... está en estado crítico. El sistema inmunoalterado no respondió bien a las modificaciones celulares."
    voice "Helena_201.mp3"
    he "Está viva..."
    voice "Helodia_56.mp3"
    el "Necesito tu habilidad."
    voice "Helena_202.mp3"
    he "¡No voy a comer más carne!"
    voice "Helodia_57.mp3"
    el "Si no lo haces... muere."
    nvl clear
    voice "N325.mp3"
    nvle "Silencio. Helena tiembla. Mira la bandeja."
    voice "Helodia_58.mp3"
    el "Tú decides. Pero el tiempo no es tu aliado."
    voice "Helena_203.mp3"
    he "¡Tú la enfermaste!"
    el "Ella se debilitó por su apego. Por ti. Sólo estoy haciendo lo necesario."
    show secuaz perro at left
    nvl clear
    voice "N326.mp3"
    nvle "La señal es clara. Uno de los secuaces le abre la boca a la fuerza. El otro coloca el trozo de carne en su lengua."
    voice "N327.mp3"
    nvle "Helena se retuerce. Llora. Traga sin querer."
    voice "N328.mp3"
    nvle "Y entonces... {p=1.5} El mundo se rompe."
    scene bg calle with fade1
    nvl clear
    show hortensia at leftdialogue
    voice "N329.mp3"
    nvle "Hortensia. Sonriente. Entregando carne a una figura oscura. Un trato. Un falso acuerdo. Una trampa. Una puerta que se cierra con violencia. El grito ahogado. Los días de encierro. Las voces apagadas. Las promesas rotas."
    scene bg hortensia labb
    nvl clear
    voice "N330.mp3"
    nvle "Y en todo eso, Hortensia escribe en la pared, una y otra vez: Helena. Helena. Helena."
    voice "N331.mp3"
    nvle "Su amor convertido en mantra."
    scene bg vomito sec with fade3
    nvl clear
    voice "N332.mp3"
    nvle "La visión se rompe. La carne cae de su boca. Vomita. Llora como si algo en su pecho hubiera explotado. No hay grito que alcance para lo que siente."
    
    scene bg lab with fade3
    nvl clear
    show helena esclava at center
    voice "Helena_204.mp3"
    he "¡La mataste!"
    show i_el_tres at rightdialogue with dissolve
    voice "Helodia_59.mp3"
    el "La guiaste hacia eso. Tu silencio. Tu duda. Yo solo... le di un fin útil."
    nvl clear
    voice "N333.mp3"
    nvle "Se acerca, le levanta la barbilla con un dedo."
    voice "Helodia_60.mp3"
    el "Y si no te decides pronto... Adara puede acompañarla."
    

    ###### Confinamiento ######################
    #################################################
    scene bg lab with fade3
    nvl clear
    voice "N334.mp3"
    nvle "Las cadenas que sostienen a Helena ahora la atan por ambos tobillos."
    voice "N335.mp3"
    nvle "No habla desde hace días. No ha dormido. A veces respira tan lento que parece parte de las paredes. Un bulto que ha decidido morir sin morir."
    voice "N336.mp3"
    nvle "Elodia observa una pantalla. Se muestra la imagen de Helena sentada en la oscuridad, inmóvil, como si el tiempo no pudiera pasar en esa habitación. Un vaso con agua sin tocar. Un trozo de carne ya enmohecido."
    show secuaz coyote at left
    voice "N337.mp3"
    nvle "Un secuaz entra. Lleva una caja de metal sellada y una jeringa."
    voice "Secuaz1.mp3"
    s1 "Nueva muestra. 7 ml. Todo estable. Sin resistencia."
    nvl clear
    show i_el_frente at right with dissolve
    voice "N338.mp3"
    nvle "Elodia recibe la jeringa y la gira contra la luz. El líquido rojo denso se desplaza lentamente."
    voice "Helodia_61.mp3"
    el "Eso es."
    voice "Helodia_62.mp3"
    el "Sin conflicto, la evolución fluye mejor."
    nvl clear
    voice "N339.mp3"
    nvle "La jeringa es depositada en un contenedor junto a varias más. Cada una marcada con códigos, fechas y un simple nombre: H.L."
    
    nvle "Elodia da un sorbo a su taza de té. Observa el monitor."

    scene bg amarillo elodia with fade3
    voice "Helodia_63.mp3"
    el "Gracias, Helena."

    scene bg lab with fade3
    nvl clear
    show helena esclava at center
    nvle "Pasos. Lentos. Precisos."
    nvle "La puerta se abre con un chirrido que retumba en el metal. Elodia entra, como si visitara una exposición de arte. Lleva una charola envuelta en tela blanca."
    nvle "Se detiene frente a Helena, quien no la mira. No la reconoce. Tal vez ya no quiere."
    nvle "Elodia destapa la charola. Un nuevo trozo de carne. Esta vez, diferente. El color más oscuro. Las fibras visiblemente humanas. Cortes precisos."
    nvle "Helena no reacciona."
    nvle "Elodia extiende la carne. Se la da de comer a Helena. Helena la ve. La reconoce. No necesita que se lo digan. Helena cierra los ojos. No gime. No tiembla. Sólo dos lágrimas silenciosas ruedan por su rostro sucio."
    nvle "Elodia se marcha. La puerta se cierra. Nadie dice nada."
    scene bg rojo carne with fade2
    nvl clear
    nvle "Helena toma otro trozo de carne a la boca con las manos temblorosas. No por hambre. No por obediencia. Por deseo de verla una vez más. Por saber si fue verdad."
    nvle "Lo muerde. Traga. Y entonces el mundo vuelve a sangrar."
    scene bg adara casa with fade1
    nvl clear
    show helena espalda at right
    nvle "Adara. Sonriendo. Escondida detrás de una pared, observando a Helena mientras riega las plantas."
    scene bg cama with fade3
    nvl clear
    nvle "Adara abrazándola por la espalda mientras duerme."
    scene bg lab with dissolve
    show adara secuestro at center
    nvle "Y luego, Adara golpeando una pared. Gritando su nombre. Intentando escapar. Pero ya era tarde."
    scene bg rojo helena with fade1
    nvl clear
    nvle "Helena abre los ojos. No hay alarido. No hay fuerza para destruir. Sólo llanto."
    voice "N354.mp3"
    nvle "La carne cae de su mano. Su cabeza se apoya contra la pared. {p=1.5} Helena solamente desea morir."


    ###### FINAL 2 Esclava de Elodia#################
    #################################################
    
    $ final_arbol = True
    scene black with fade1
    show screen arbol_screen with fade1
    ""
    ""
    ""
    ""
    return


#FIN