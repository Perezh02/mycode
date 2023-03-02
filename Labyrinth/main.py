#!/usr/bin/env python

import random
print("""
Can you Escape the Mental Prison!
You find yourself in the entrance of a dark labyrinth. Your goal is to navigate through the labyrinth and find the treasure hidden at the end. Good luck!
 
 """)


# Define the labyrinth map
labyrinth = {
    'entrance': {
        'description': 'As you start to wake up, you find yourself in the entrance room of a grand old mansion that resembles an ancient Victorian queens palace. The details are intricate and the charm of the old-world is evident. However, as you begin to take in your surroundings, you realize that something is not quite right. The furniture and decor appear to be distorting and warping, forming strange and unfamiliar patterns and shapes. Something is wrong.  You notice that the characteristics of this queens residents seems to be sponnger the familiar feeling of hard wood. The room is different but subtleness of this difference is not important now, because as you try to make sense of your surroundings, a clock screams 11 minutes 35 seconds as the walls begin seep a red substance that is rapidly filling the room.  There are two doors but where they go is unknown.  Do you take the north or do you take the door to the east... indecision means death as the room slight gasps at the reality there is a form object dwelling in it.',
        'items': [],
        'exits': {'north': 'north1', 'east': 'east1'}
    },

    'north1': {
        'description': 'You choose to take the door leading north, hoping that it will lead you out of this strange and terrifying room. As you enter the next room, you notice that it is much darker and colder than the entrance room. The walls seem to be made of spongy stone, and the only light comes from a dimly glowing orb in the center of the room. You can feel the weight of the silence and the stillness of the air around you, and you wonder if you are truly alone in this bizzare labyrinth. As you begin to take a step forward, you suddenly feel a presence behind you. You turn around to see a shadowy figure lurking in the darkness, watching your every move. You freeze, unsure of what to do next, as the figure seems to be closing in on you. You realize that you must act quickly if you want to survive this labyrinth and escape with your life.',
        'items': [''],
        # it would be cool to have a name input
        'exits': {'freeze': 'freeze', 'north': 'north2', }
    },

    'north2': {
        'description': 'reduce text:  As you take the door leading north, the unsettling feeling in your gut only grows stronger. The hallway is dimly lit, and the air is thick with a musky scent that makes it hard to breathe. The walls are slick with moisture, and you can hear the sound of your footsteps echoing eerily down the corridor. Suddenly, you catch a glimpse of one shadowy figure moving in the distance. As it gets closer, you see that its a creature with the body of a Satyr, the wings of a moth, and the tentacles of an octopus. It seems to be studying you with a wary eye, as if unsure whether to trust you or not. As you take a step forward, the creature suddenly perks up its ears and begins to move in a rhythmic motion to what seems like a wonderful world. You notice that this creature is responding to the faint sound of music thats coming from somewhere. this moment is brief but distinct.... The creature recoils as the music stops like it had awoken to a foriegn agent staring at them. You take step closer, the creature takes a step back. Tension is building when you see a recorder flute Mysteriously placed next to a white picket fence near a fountain made of brozen representing pigs playing in a bath. You wonder if playing the flute might be the key to winning its trust. Or should you just press ahead... Time is running out',
        'items': ['flute'],
        'exits': {'north': 'north3', 'west': 'north2west1', 'east': 'north2east1', 'south': 'north1', 'playflute': 'flute'}
    },

    'north3': {
        'description': 'As you take the door leading north, panic sets in as the struggle for oxygen begins to intensify. The air is thick and oppressive, making it difficult to catch your breath. You feel as if the oxygen is being sucked from your chest, leaving you gasping for air. You stumble forward, desperate to find a way out of this suffocating hallway. Do you keep pressing forward or do you you jest give up? As you move forward, you try to focus on finding a way out of the suffocating hallway. You can feel your body starting to shut down, and you know that you need to get out before its too late. But the air seems to be getting thicker and more suffocating with each passing moment. At this point, you have a choice to make. Do you keep pressing forward, driven by desperation and the need to survive? Or do you give up, overwhelmed by the intensity of the situation? The decision is yours, but you know that your life hangs in the balance.',
        'items': [],
        'exits': {'north': 'north4', 'south': 'north2', 'laydown': 'die'}
    },

    'north4': {
        'description': 'As you stumble forward, gasping for air, you push yourself through the door leading north. To your relief, oxygen floods into your lungs and the panic subsides. You take deep breaths, savoring the clean air and the feeling of relief that washes over you. But as you look around, you realize that you are not out of danger yet. You are faced with a puzzle that looks like the key to a gate made of sharp iron posts. The posts glint menacingly in the dim light, and you can feel your heart rate increasing again. You study the puzzle, trying to make sense of the symbols and shapes. But its confusing, and you cant seem to find the right combination of moves to solve it. Frustration builds inside you as you realize that you need to solve this puzzle to progress. You know you cant go back, so you press forward, determined to find a way to solve the puzzle and open the gate. With each passing moment, the urgency and the pressure increases. You can feel your mind racing as you try to come up with a solution. At this point, the decision to keep pressing forward is no longer just about survival - its about finding a way to escape this maze and uncover the secrets within. You know that the stakes are high, and failure is not an option. So, with a deep breath, you steel yourself for the challenge ahead and prepare to take on the puzzle.',
        # guess a number between 1 and 1000 in 5 tries
        'items': ['puzzle one'],
        'exits': {'north': 'north5', 'south': 'die', 'east': 'north4east1'}
    },

    'north5': {
        'description': 'As you push through the iron leading north, you hear a low growl coming from the darkness ahead. Your heart sinks as you realize that you are not alone in this maze. Suddenly, a massive creature emerges from the shadows, its eyes glowing with a fierce hunger. The creature is unlike anything you have ever seen before. It towers over you, with rippling muscles and razor-sharp claws that glint in the dim light. Its skin is tough and impenetrable, and you know that you have no chance of defeating it without some kind of weapon. As the creature advances on you, you feel a surge of fear and desperation. You know that staying to fight means certain death, and your only hope is to retreat and find another way out of this maze. You turn to run, but the creature is too fast. It lunges forward, its jaws snapping shut just inches from your face. You can feel the heat of its breath on your skin, and you know that you are running out of time. With a burst of adrenaline-fueled strength, you manage to break free of the creatures grasp and race back through the door you came from. Your heart is pounding in your chest as you sprint down the hallway, back the way you came. As you run, you realize that you need to find a new path through this maze - one that doesnt involve facing off against that monster again. You take a deep breath, trying to calm your racing thoughts, and prepare to press on into the unknown.',
        'items': [],
        # NEED TO FIGURE OUT HOW TO ALLOW THE DIE TO CHANGE ONCE THE PLAYER HAS A SWORD AND A POTION
        'exits': {'north': 'die', 'west': 'north5west1'}
    },

    'north6': {
        'description': 'You grip the hilt of your sword tightly as you enter the room to the north, ready for whatever might come your way. The air is chilly, and the darkness seems to seep into your bones. You take a cautious step forward, trying to keep your eyes peeled for any movement. Suddenly, you hear a low growl coming from behind you, and you spin around to face the monster. Its a massive creature with razor-sharp claws and glowing red eyes, and its moving towards you with lightning-fast speed. You raise your sword and prepare for battle, but the creature is too fast and too strong. Its claws strike out at you, and you barely manage to dodge out of the way. You feel a cold sweat break out on your forehead as you realize that this monster is not to be underestimated. You quickly gulp down the potion you brought with you, feeling a sudden surge of strength and energy. The battle is fierce and intense, and youre not sure if youll make it out alive. You swing your sword with all your might, but the monster is relentless. It claws at you with its razor-sharp talons, and you feel the sting of its blows. Your heart is pounding in your chest, and you know that you need to find a way to defeat this creature before its too late. Just when you think all is lost, you notice a small opening in the creatures armor. With a swift strike, you plunge your sword into the gap, and the monster lets out a deafening roar. It falls to the ground with a thud, defeated. Breathless and exhausted, you take a moment to catch your breath. You realize that youre lucky to be alive, and you know that you need to be more careful as you press on into the labyrinth. You wipe the sweat from your forehead and steel yourself for whatever might come your way next.',
        'items': [],
        'exits': {'north': 'north7', 'south': 'north5'}
    },

    'north7': {
        'description': 'As you explore the next room, you see a locked door in the distance. You try to open it, but it doesnt budge. You examine the lock, but it seems to be magically sealed. Frustrated, you turn around and notice a friendly spirit floating towards you. As she comes closer, you see a key hanging from her neck. She greets you warmly and asks if you need help. You explain your situation, and she nods understandingly. However, she tells you that she cannot simply give you the key - you must prove that you are worthy of it. She explains that she requires three items: three Keys. If you have these items, she will heal you and give you the key. If not, you must go back and find them.'

        'You rummage through your backpack and breathe a sigh of relief as you find the items she needs. You hand them over to her, and she smiles kindly. She takes the items and begins to chant a healing spell. You feel a warm sensation spreading throughout your body, and your wounds start to close up. Your exhaustion fades away, and your strength returns. You thank the spirit gratefully, and she hands you the key. As you turn to leave, she warns you of the challenges ahead and advises you to be careful. You nod, knowing that you are ready to face whatever comes your way. You insert the key into the lock and turn it, feeling a sense of satisfaction as the door creaks open. You step through the threshold, ready to face the next challenge of the labyrinth.',
        'items': [],
        'exits': {'north': 'north8', 'south': 'north6', 'east': 'north7east1'}
    },

    'north8': {
        'description': 'As you enter the next room, a sense of dread washes over you, and the hairs on the back of your neck stand up. The sign on the wall reads "Can you Escape the Mental Prison!", and you know that Paul, the warping and shifting presence, is lurking nearby. You try to push forward, but the door ahead is sealed tight, and you feel exhaustion starting to distort your perception, adding to the confusion. Suddenly, Paul, the aggressive and unkind Magi, materializes in front of you, blocking your way. He tells you that you must prove your worth by completing three puzzles, and gestures towards a table in the center of the room, where three puzzle boxes sit, each one more intricate than the last. As you work on the puzzles, you feel Pauls presence looming over you, making it hard to focus. His aura is so overwhelming that you start to feel like youre losing your mind.',
        'items': [],
        'exits': {'north': 'finish', 'south': 'north6', 'west': 'hidden ending'}
    },
    'east1': {
        'description': 'As you open the door to the east, you find yourself in a narrow and scary hallway. The walls are adorned with strange patterns and symbols that seem to shift and distort as you walk by, adding to the suspense. As you move forward, you notice a door at the end of the hallway, but the fear of what lies beyond it sends shivers down your spine. The hallway fills with a red substance, and you realize with horror that it is the blood of past explorers who entered this mental labyrinth. The names of the fallen are written on the walls, a haunting reminder of the dangers that lie ahead. The air is thick with the stench of death and decay, and you can hear the faint whispers of lost souls calling out for help. The fear of the unknown is overwhelming, and you wonder if you made the wrong choice in taking this path. You must be careful not to succumb to the fear and the exhaustion that threatens to distort your senses and cloud your judgment.',
        'items': [],
        'exits': {'east': 'east2', 'west': 'entrance'}
    },

    'east2': {
        'description': 'You open the door to the east and find yourself in a long, dimly lit hallway. As you take a step forward, the floor creaks beneath your feet, and you hear a faint whisper in the distance. The walls are lined with old, tattered tapestries that depict scenes of battle and destruction. You notice that the tapestries seem to move ever so slightly as you pass them, almost as if they are alive. The air is thick with the smell of must and decay, and you can feel the weight of the unknown pressing down on you. As you move deeper into the hallway, you see a faint light in the distance, and you feel a sense of hope rise within you. However, as you get closer, you realize that the light is coming from a room filled with bones and skulls. The door is slightly ajar, and you can see the faint outline of something moving inside. The fear grips you, and you wonder if you should turn back, but you know that you must push forward if you want to survive. The question is, will you be able to face whatever lies ahead?',
        'items': [],
        'exits': {'east': 'east3', 'west': 'east1'}
    },

    'east3': {
        'description': 'As you enter the next room, you feel a sense of relief that youve made it through the hallway. However, that relief is short-lived as you notice that there are two doors in front of you. The one to the north is completely broken down with blood and death surrounding it while the one to the east looks normal. The choice is yours to make, but you cant shake off the feeling that something terrible awaits you regardless of which door you choose. As you approach the doors, you hear faint whispers and the sound of something scratching against the walls. You try to push the thoughts of danger out of your mind and focus on the task at hand. Which door do you take?',
        'items': [],
        'exits': {'north': 'north1east3', 'east': 'east4', 'west': 'east2'}
    },

    'east4': {
        'description': 'You choose the door to the east and enter into a small room. The room is completely empty except for a single pedestal in the center, with a small keyhole in it. You realize that you must find the key to unlock the door that lies ahead. As you search the room, you hear a low growling sound coming from the darkness. You know that you are not alone in this room, and the fear sets in. You must find the key quickly and leave before whatever is lurking in the shadows finds you. The question is, can you keep your nerves together and find the key before its too late?',
        'items': ['key'],
        'exits': {'east': 'east5', 'west': 'east3'}
    },

    'east5': {
        'description': 'You insert the key into the door and turn it, the lock clicks and the door creaks open. You enter into a large, open space that seems to stretch on forever. The darkness is thick and oppressive, making it difficult to see beyond a few feet in front of you. You can hear strange noises coming from all around you, and you realize that you are not alone in this place. As you move forward cautiously, you see movement in the shadows, but you cant quite make out what it is. The air is heavy with the stench of decay, and you can feel the weight of death all around you. Suddenly, you hear a loud, guttural roar that echoes throughout the room. Whatever it is, it is coming closer, and you know that you must act fast if you want to survive. Will you face whatever lies ahead, or will you turn and run for your life?',
        'items': [],
        'exits': {'east': 'east6', 'west': 'east4'}
    },

    'east6': {
        'description': 'This room is much larger than the others, and the air is thick with a musty scent that makes it hard to breathe. You feel the weight of the darkness pressing down on you as you take a step forward. Suddenly, you hear a blood-curdling scream that echoes throughout the room, and the shadows come to life. You try to run, but the shadows attack you, devouring your sense of reality causing a mental distortion so powerful that it consumes you entirely. You lose all sense of reality, and you find yourself in a dark void where there is no escape. death is now your only option. so you wait ',
        'items': [],
        'exits': {'death': 'entrance'}  # fix this logic
    },

    'north1east3': {
        'description': 'As you open the broken down door to the north, you find yourself in a narrow and claustrophobic hallway. The walls are covered in a thick layer of cobwebs and the air is stale and musty. As you move forward, you hear the sound of something slithering in the shadows, and you feel a chill run down your spine. The darkness seems to be alive, pulsing and breathing, and you realize that you are not alone. You can hear the whispers of the dead and the groans of the damned, and you know that you must find a way out before the shadows consume you. As you look around, you see a faint light in the distance, and you feel a glimmer of hope. You move towards the light and find a torch that flickers to life when you light it. The torch illuminates the darkness, and the shadows keep their distance, but you can still feel them pressing in, waiting for their chance. You must keep moving forward, torch in hand, and find a way out before its too late.',
        'items': ['torch'],
        'exits': {'north': 'north2east3', 'south': 'east3'}
    },

    'north1west2': {
        'description': 'As you crawl through the narrow opening in the wall, you can feel your heart racing with fear and anticipation. The adrenaline from your recent encounter is still coursing through your veins, and you know that you need to keep moving if you want to survive. You are alone in the darkness, and the only sound you can hear is the beating of your own heart. But your peace is short-lived, as you hear the sound of the creatures following you growing louder and closer. They are catching up, and you know that you need to fight for your life once again. You take out your sword, ready to face the oncoming threat. The creatures burst into the small space, their eyes glowing in the darkness. You fight them with all your might, striking them down one by one. But no matter how many you kill, more keep coming. You start to feel the exhaustion weighing down on you, your arms growing heavy with each swing+. You start to realize that you made a mistake by underestimating the dangers that lurk in this labyrinth. You should have been more careful, more vigilant, and less careless. But its too late now. The creatures overtake you, their claws digging into your flesh. You fight for a few more moments, but you know that its too late. You are going to die in this labyrinth, just another victim of the dangers that lurk in the darkness. As you take your last breath, you feel a sense of regret wash over you. You realize that you made a fatal mistake, and it cost you your life. The plot thickens, and you are left wondering what other dangers and challenges await those who dare to enter the labyrinth.',
        'items': [''],
        'exits': {'death': 'entrance'}
    },

    'north2east1': {
        'description': 'As you enter the next room through the door to the east, you find yourself in a dimly lit room with a strange aura. You can feel an unnatural presence in the air, and the hair on the back of your neck stands on end. The walls are covered in strange symbols and runes (U) that seem to glow in the dim light, and you can hear a faint chanting coming from somewhere in the room. As you take a step forward, the floor creaks, and you see a strange mist rising from the cracks. The mist is cold and damp, and you can feel it seeping into your bones. You realize that you must find a way out of this room before its too late, but the exit is not immediately clear. You see two doors on opposite sides of the room, and you wonder which one will lead you to safety. You must choose quickly, for the chanting is growing louder, and the mist is thickening, threatening to consume you completely.',
        'items': [],
        'exits': {'east': 'north2east2', 'west': 'north2'}
    },

    'north2east2': {
        'description': 'As you step through the door to the east, you find yourself in a dark and foreboding hallway. The walls are covered in strange runes (P) that seem to writhe and twist in the dim light. You can hear the sound of something moving in the shadows, and you feel a sense of unease that grows stronger with each passing moment. Suddenly, you hear a low growling sound, and you realize that you are not alone. You see a pair of glowing eyes staring at you from the darkness, and you know that whatever is lurking in the shadows is not friendly. You try to move forward, but the growling gets louder, and you can hear the sound of something breathing heavily. You start to panic, but then you notice a figure hiding in the shadows. Its a mysterious character that seems to be watching you. You cant tell if they are friend or foe, but they seem to be trying to communicate with you in some way. The tension in the room is almost unbearable, and you feel your heart racing as you try to make sense of the situation. You realize that you must choose your next move carefully, for your survival depends on it. Will you trust the mysterious figure and follow their lead, or will you try to make a run for it and hope for the best? The choice is yours, but the consequences of your decision could be dire.',
        'items': [],
        'exits': {'east': 'north2east3', 'west': 'north2east1'}
    },

    'north2east3': {
        'description': 'You continue down the narrow hallway, torch in hand, and notice that the shadows seem to be morphing into something different. Theyre no longer just dark and menacing, but now they seem to be pulsating with a strange energy. You can feel the hairs on the back of your neck stand up as the hallway becomes colder and colder. You can see your breath in the air, and you wonder what kind of twisted world youve stumbled into. As you reach the end of the hallway, you find yourself in a room with four doors, each leading in a different direction. The room is even colder than the hallway, and you can see your breath in the air more clearly now. The shadows in the room seem to be alive, swirling and pulsing with an otherworldly energy. You can hear strange whispers in the air, and you wonder if youre losing your mind. As you explore the room, you notice a stone in the center of the room with strange markings on it (L). As you look closer, you realize that the markings are a message of sorts, telling you how to survive in this mental prison. It reads three keys are required. The message is cryptic, but you realize that you need to keep moving forward, always forward, and never look back. Confused and disoriented, you must make a choice of which door to take next, but all you can do is follow the message on the stone and hope that you will find your way out of this twisted reality.',
        'items': [],
        'exits': {'north': 'north3east3', 'south': 'north1east3', 'east': 'north2east4', 'west': 'north2east2'}
    },

    'north2east4': {
        'description': 'As you enter the room through the door to the east, you feel a sense of dread wash over you. The room is dark, and the air is thick with an electrical energy that makes the hair on the back of your neck stand up. The walls are covered in strange markings (A), and you can hear a faint humming sound coming from somewhere in the room. As you take a step forward, you see a figure moving in the shadows, and you realize that you are not alone. The figure seems to be watching you, and you can feel its eyes on you even though you cant see its face. The tension in the room is almost unbearable, and you wonder if you should turn back, but you know that you must keep moving forward if you want to escape this place. As you explore the room, you notice that there is only one doors to the east.  You know that you must choose your next move carefully, but you cant shake off the feeling that death is lurking around every corner. Suddenly, the electrical energy in the room intensifies, and the figure in the shadows steps forward. It is a tall, imposing figure with crackling energy emanating from its body. You can feel the electricity in the air, and you realize that the figure is not human. Its eyes glow with a strange intensity, and you feel a sense of panic rising in your chest. You must make a quick decision. Will you try to fight the figure, or will you run for your life? As you contemplate your options, you notice a small stone on the ground. It seems to be pulsing with the same electrical energy as the figure, and you wonder if it has any significance. ',
        'items': ['stone'],
        'exits': {'east': 'north2east5', 'west': 'north2east3'}
    },

    'north2east5': {
        'description': 'As you enter the next room through the door to the east, you feel a sense of dread wash over you. The room is bathed in an eerie green light, and the air is thick with a toxic mist. You can barely see in front of you, and you wonder what kind of twisted world youve stumbled into. As you take a step forward, you hear a low growling sound, and you realize that you are not alone. Suddenly, the figure from the previous room emerges from the shadows, its eyes glowing with a menacing energy. Its electrical presence is stronger than ever before, and you feel a sense of impending doom. The figure speaks to you in a language you cannot understand, but its message is clear: you must fight to continue on your journey. You know that you have no choice but to face this new challenge head-on. You brace yourself for a fight, gripping the stone tightly in your hand. The figure charges towards you, and you engage in a fierce battle. The air crackles with electricity, and you feel the power of the cosmos coursing through your veins. You fight with all your might, fueled by the desire to survive and escape this place.',
        'items': ['stone'],
        'exits': {'north': 'north3east5', 'west': 'north2east4'}
    },

    'north2west1': {
        'description': 'As you move west, you find yourself in a bright, cheerful room filled with soft, fluffy pillows and blankets. The walls are painted in pastel colors, and you can hear the sound of birds chirping outside. You take a deep breath and feel a sense of peace and tranquility wash over you.You cant help but feel a sense of relief as you take in the beauty of the room. You feel safe and secure, surrounded by warmth and comfort. You take a seat on one of the pillows and close your eyes, taking in the calm and serenity of the moment.As you sit there, you realize that this is exactly what you needed - a moment of rest and relaxation in the midst of the chaos and danger of the labyrinth. You feel a sense of gratitude and appreciation wash over you, and you cant help but smile.You take a few deep breaths, feeling the tension and stress of the previous challenges melt away. You realize that you are stronger than you thought, and that you can face whatever challenges lie ahead with courage and determination. As you get up to leave the room, you notice a note on the wall. It reads: "You are strong, courageous, and capable of overcoming any obstacle. Remember to take time for yourself and to appreciate the beauty and joy in every moment. Keep going - the journey is just beginning. You feel a sense of encouragement and support wash over you as you read the note. You know that you are not alone in this journey, and that there are others out there rooting for you and cheering you on. As you leave the room and continue on your journey through the labyrinth, you feel a sense of renewed energy and determination. The challenges ahead may be difficult, but you know that you have what it takes to overcome them. You hope to maintain this feeling of serenity as you move forward. ',
        'items': [],
        'exits': {'east': 'north2', 'west': 'north2west2'}
    },

    'north2west2': {
        'description': 'You find yourself in a large, open room with high ceilings and bright lighting. The space is filled with sparkling jewels and precious stones, reflecting the light in a dazzling display. You cant help but feel an overwhelming sense of joy and wonder as you take in the beauty of the room. The moment seems too good to be true, and you cant shake the feeling that something is off. As you move further into the room, you notice a faint humming sound that grows louder and more intense with each step you take. Suddenly, the ground beneath your feet begins to shake and crumble, sending you tumbling down into a dark pit. You land hard, the wind knocked out of you, and as you struggle to regain your senses, you realize that you are not alone. You can hear the sound of breathing coming from the darkness, and you feel a sense of fear wash over you as you realize that you are trapped in the pit with some kind of creature. You cant see anything in the darkness, but you can feel its presence, and you know that you need to act quickly if you want to survive. You search through your inventory, desperate for something to defend yourself with, and you find a small vial of glowing liquid. Without hesitation, you drink the potion, feeling a surge of energy and strength course through your body. You unsheathe your sword, ready to face whatever lurks in the darkness. The creature charges at you, its eyes glowing in the dark, but you are ready for it. You swing your sword, the blade glinting in the light, and strike the creature with all your might. The creature lets out a deafening screech, and you can feel the weight of its body crash down on you. You manage to push the creature off you and scramble to your feet, panting heavily. You realize that you are not out of danger yet and that you need to find a way out of this pit before something else comes after you. The adrenaline is pumping through your veins, and you can feel the fear and the excitement mingling inside you as you prepare to face whatever lies ahead. As you look around, you notice a small opening in the wall, just big enough for you to crawl through. You hesitate for a moment, wondering if this is the right way to go, but you know that you need to keep moving if you want to survive. You take a deep breath and crawl through the opening, the darkness closing in around you. The plot thickens, and you are left wondering what other dangers await you as you continue your journey through the labyrinth.',
        'items': [],
        'exits': {'north': 'north3west2', 'south': 'north1west2', 'east': 'north2west1'}
    },

    'north3east3': {
        'description': 'As you enter the next room through the door to the north, you feel a sense of dread wash over you. The air is thick and heavy, and the darkness seems to have a physical weight. You can hear strange whispers in the air, and the shadows seem to be alive, pulsing with an otherworldly energy. You know that you must keep moving forward, but the path ahead is uncertain. As you explore the room, you notice that there are no doors or windows, and you realize that you are trapped. Panic sets in as you try to find a way out, but there seems to be no escape. Suddenly, a clock on the wall starts to scream, and the sound is deafening. You feel a sense of urgency, and you know that time is running out. The walls start to bleed, and you can see the red liquid dripping down the walls. The floor beneath your feet starts to shake, and you realize that the room is collapsing. You must find a way out, but the only choice is to move forward. As you take a step forward, the room starts to crumble around you, and you wonder if this is the end. You must keep moving forward, one step at a time, and hope that you will find a way out before its too late.',
        'items': [],
        'exits': {'north': 'north4east3', 'south': 'north2east3'}
    },

    'north3east5': {
        'description': 'You manage to defeat the figure and breathe a sigh of relief as its electrical energy dissipates into the air. The room starts to brighten, and the toxic mist begins to clear, revealing a small key on the ground with the letter (L) on it. You pick it up, feeling a sense of triumph wash over you. Finally, you have one of the keys needed to escape this mental prison. As you examine the room further, you notice that there is only one door leading north. You know that you must keep moving forward, but suddenly, a clock in the room starts to scream, its hands spinning wildly. You feel a sense of panic rising in your chest as the halls around you start to bleed at a quicker rate. You know that time is running out, and you must hurry if you want to survive. With the key in hand, you move forward through the only available exit, hoping that you will find a way out of this twisted reality before its too late.',
        'items': [],
        'exits': {'north': 'north4east5', 'south': 'north2east5'}
    },

    'north3west2': {
        'description': 'As you run through the maze, you can feel the creatures closing in on you, their claws scraping against the walls. You know that you have to fight for your life, and that every second counts. You think back to how you ended up here, trapped in this mental prison. It started with a simple job, a quick heist that was supposed to be easy. But something went wrong, and you ended up getting caught. The authorities sentenced you to life on a new pharma test drug, a drug that is rumored to drive its inmates to the brink of insanity. You knew that you had to escape, and so you started planning. You spent months studying the the mental effects of this drug, learning its secrets and weaknesses. And finally, you found your chance to break free the guards set the creatures loose on you, their twisted experiments unleashed to hunt you down. You had no choice but to run, to fight, to do everything you could to stay alive. Now, as the creatures catch up to you, you feel a fierce determination rise up inside you. You are not going to die in this place, not after everything youve been through. You fight with all your might. You manage to push them back for a moment, but they regroup, their eyes glowing in the dark. And then, in one swift movement, they charge you.',
        'items': [],
        # fight then can move
        'exits': {'north': 'north4west2', 'south': 'north2west2', 'west': 'north3west3'}
    },

    'north3west3': {
        'description': 'As you exit the collapsing room, you find yourself in a narrow hallway. The walls are made of cold stone, and you can hear the distant sound of running water. You try to catch your breath, but the adrenaline is still pumping through your veins. As you look around, you notice a puzzle in the middle of the room. The puzzle consists of a series of strange symbols etched into the stone. You can feel the weight of the previous challenges bearing down on you, and you realize that you are not out of danger yet. You remember the one-liner from the previous room, "Survival is not guaranteed, but it is worth fighting for." The words echo in your mind, and you realize that you must solve the puzzle if you want to survive. You study the symbols carefully, trying to make sense of them. Suddenly, you have a breakthrough. You realize that the symbols are a code, and that each one represents a different letter of the alphabet. You start to decipher the code, your heart racing with excitement. Finally, after what feels like hours, you solve the puzzle. As you enter the solution, a hidden door opens, revealing a small key with the letter (M) on it. You take the key, feeling a sense of relief and satisfaction wash over you. You know that you are one step closer to escaping this mental prison. As you move forward, you cant help but wonder what other challenges await you on this journey.',
        'items': [],
        'exits': {'east': 'north3west2'}
    },

    'north4east1': {
        'description': 'As you stumble forward, gasping for air, you push yourself through the door leading east. A sense of relief washes over you as you realize that you have escaped the previous level. But as you look around, you realize that you are in a strange, surreal environment. The world around you is distorted, and you start to question your sanity. You wonder if this is all a dream or if you have been driven to madness by the trials you have faced so far. The clock in the distance starts to scream, reminding you that time is limited, and you feel a sense of overwhelming dread. You start to question your ability to continue this journey, feeling the weight of the reality that you may not survive if you make a mistake. You try to push these thoughts aside and focus on the task at hand, but they continue to linger in the back of your mind. As you move forward, you come across a puzzle that seems to be a key to a gate made of jagged glass shards. The shards glint menacingly in the dim light, and you can feel your heart rate increasing again. You study the puzzle, trying to make sense of the symbols and shapes, but it seems impossible to solve. The urgency and pressure increase as the clock continues to scream, and you can feel the weight of the situation bearing down on you. You know that you have to solve this puzzle to progress, and failure is not an option. With each passing moment, your energy starts to drain, and you wonder how much longer you can hold on. But you take a deep breath and remind yourself that you have come too far to give up now. You steel yourself for the challenge ahead, ready to take on the puzzle and find a way to escape this nightmare',
        'items': [],
        'exits': {'west': 'north4', 'west': 'north4east2'}
    },

    'north4east2': {
        'description': 'As you step through the door leading east, you find yourself in a dark, foreboding cavern. The air is thick with the stench of decay, and you can feel a sense of dread settling over you. The clock in the distance starts to scream, reminding you that time is limited, and you start to question your decision to continue this journey. You wonder if this is all a figment of your imagination or if you have been plunged into a twisted, alternate reality. The confusion and doubts start to impact your energy, causing you to feel weaker and more vulnerable. As you move forward, you come across a group of creatures that seem to have been waiting for you. The clock continues to scream in the distance, and you feel a sense of overwhelming dread.',
        'items': [],
        'exits': {'north': 'north5east2', 'east': 'north4east3', 'west': 'north4east1'}
    },


    'north4east3': {
        'description': 'As you cautiously move forward, you notice a buzzing sound growing louder and louder. Suddenly, you are swarmed by a group of flying creatures with sharp teeth and stingers. You try to fight them off, but they seem to be everywhere, attacking from all angles. Panic sets in as you realize that they are too many and too fast for you to handle. But then, you notice something different about one of the creatures - its wearing a crown. You realize that this must be the leader of the swarm, and that defeating it might be the key to survival. With a newfound sense of determination, you focus your attacks on the crowned creature, dodging and weaving through the swarm. You can feel their bites and stings all over your body, but you push through the pain, driven by the will to survive. The clock in the distance continues to scream, reminding you that time is running out. With each passing moment, the urgency and pressure increase, and you know that you must act fast.',
        'items': [],
        # need to fix!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        'exits': {'north': 'north5east5', 'south': 'north3east5', 'fight': ''}
    },

    'north4east5': {
        'description': 'As you move north, the memories of all the dead come to life in your subconscious, tormenting you with all the times you hurt someone in your past. You feel the weight of the destruction you have caused in your life, and its almost suffocating. You try to shake off the feeling, but its like a heavy cloak that you cant escape from. The clock continues to scream at you, reminding you that time is limited, and you must keep moving forward. The hallway you find yourself in is long and narrow, with strange markings (X) covering the walls. You can hear the sound of whispers in the air, and you feel a sense of unease creeping up on you. Suddenly, you hear a low growling sound, and you see a pair of glowing eyes in the darkness. You realize that you are not alone, and that something is stalking you. You grip the key tightly in your hand, ready to fight if you need to. The figure emerges from the shadows, and you see that it is a grotesque creature with razor-sharp claws and teeth. Its eyes gleam with a feral hunger, and you know that if you fight you wont survive. Creatures claws tear into your skin.  Fueled by the memories of your past and the desire to escape this place you run. As the creature falls to the ground with the intention of destroying you. You catch a glimpse of a door to the north. You know that you must get out of this room, now, but the weight of your past is almost too much to bear. You wonder if you will ever be able to escape the mental prison that you are trapped in. Is it even worth it',
        'items': [],
        # add Fight die
        'exits': {'north': 'north5east5', 'south': 'north3east5'}
    },

    'north4west2': {
        'description': 'As you take the key and move forward, you find yourself in a vast, open space. The air is thick and humid, and you can feel the sweat starting to bead on your forehead. You look around, trying to get your bearings, but the darkness seems to stretch on forever. Suddenly, you hear a sound in the distance. Not again races through your head, over and over. Somthing is out there. you need to keep moving if you want to survive. You run through the darkness, your heart pounding in your chest, your feet pounding against the spoongy ground. You can hear behind you but you dont want to look. their breath hot on your neck. You know that you must keep moving forward, no matter what. As you run, you notice a faint light in the distance, and you realize that it might be your way out. You pick up your pace, your resolve strengthening with each step. Finally, you reach the light, and you burst through the door, gasping for breath. You find yourself in a brightly lit room. You look around, trying to get your bearings, and you realize that you are outside. But it doesnt look like the outside.  Its something different. You take a deep breath, because your journey is not over. So you move',
        'items': [],
        'exits': {'north': 'north5west2', 'south': 'north3west2'}
    },

    'north5east2': {
        'description': 'As you enter the room, you feel a sense of unease wash over you. The room is dark and foreboding, with a strange energy pulsing through the air. You take a step forward, and suddenly, you see your reflection in the mirror. But its not just any reflection - its your evil self, your false self. The part of you that you dont want to face but cant escape from. Your heart races as you realize that you must face yourself if you want to continue on your journey. The reflection steps out of the mirror, and you feel a surge of fear and panic. It looks just like you, but its eyes gleam with a sinister energy that youve never seen before. You grip your weapon tightly, ready to fight if you have to. The reflection charges towards you, and you engage in a fierce battle. The fight is intense, with neither of you gaining the upper hand. You realize that you are fighting not just for your survival but for your soul. The clock in the room screams at you, reminding you that time is limited, and you must defeat your evil self before its too late. As the battle rages on, you start to question who you really are. Are you the person you want to be, or are you just a reflection of your past mistakes? The weight of your inner turmoil almost becomes too much to bear, but you know that you cant give up. You must defeat your evil self and move forward if you want to escape this twisted reality.',
        'items': [],
        'exits': {'reflect': 'north6east2'}
    },

    'north5east5': {
        'description': 'As you run towards the door to the north, the creature continues to chase after you. Its claws scrape against the walls, leaving deep gouges in the stone. You can feel its hot breath on the back of your neck, and you know that you must keep moving or die. The clock in the room continues to scream at you, its hands spinning faster and faster. Time is running out, and you wonder if you will ever make it out alive. As you burst through the door, you find yourself in a large room with a single torch flickering on the wall (Y). The room is dimly lit, and you can barely see anything in front of you. You try to catch your breath, but the memories of your past continue to torment you. You feel like giving up, like theres no point in continuing on. But then you remember the key in your hand, and the hope that it represents. You know that you must keep moving forward, no matter how hard it seems. Suddenly, you hear a strange clicking sound, and you realize that the creature is still chasing after you. You can hear its heavy breathing, and you wonder how much longer you can keep running. You know that you must find a way to escape, and fast. Do you fight or do you keep running',
        'items': [],
        # add fight will die
        'exits': {'north': 'north6east5', 'south': 'die', 'fight': 'die'}
    },

    'north5west1': {
        'description': 'As you engage in battle with the creature, you start to realize that it is not like the others youve faced before. Its movements are more fluid, its attacks more calculated. You start to wonder if this is all part of the mental prison, if these creatures are manifestations of your own fears and doubts. The clock in the distance seems to be getting louder, and you can feel the pressure of time weighing down on you. You know that you must defeat this creature quickly if you want to keep moving forward. Your mind races as you try to come up with a strategy, but the confusion and doubts keep creeping up on you. You start to feel your energy draining, your movements becoming sluggish. You cant afford to lose focus now, not when your life is on the line. With a burst of determination, you channel all your energy into a final blow, and the creature falls to the ground, defeated. As you catch your breath, you start to wonder if this is all worth it. Is the risk of losing your sanity worth the chance of escaping this mental prison? But you know that you cant give up now. You take a deep breath and push forward, ready to face whatever challenges lie ahead.',
        'items': [],
        'exits': {'east': 'north5', 'west': 'north5west1'}
    },

    'north5west2': {
        'description': 'As you step out of the bright room, you find yourself in an eerie forest. The trees are twisted and gnarled, their branches reaching out like claws. The air is thick with mist, and you can hear strange noises coming from all around you. You start to feel a sense of confusion creeping up on you, wondering if this is all real or just a part of your mind. The clock in the distance continues to scream, reminding you that time is running out. You start to feel overwhelmed, the doubts and confusion starting to impact your energy. You feel a sense of dread as you realize that you have to keep moving forward, no matter what. You take a deep breath and push through the fog, determined to find a way out of this mental maze. As you move forward, you come across a clearing, and you see a figure standing in the distance. You cant quite make out who or what it is, but you feel a sense of unease. You try to move quietly, but a twig snaps under your foot, alerting the figure to your presence. It turns to face you, and you realize that it is one of the creatures that had been chasing you earlier. Its eyes lock onto yours, and you know that you must fight for your life once again. Your resolve strengthens, and you charge towards the creature, ready to face whatever comes your way.',
        'items': [],
        'exits': {'east': 'north5west1', 'west': 'north5west3'}
    },


    'north6east2': {
        'description': 'As you enter the room to the north, you feel a sense of unease wash over you. The air is thick with a cloying mist, and the room seems to be pulsating with a strange energy. You can hear strange whispers in the air, and you feel a sense of dread creeping up on you. You try to shake off the feeling, but its like a weight on your shoulders that you cant escape from. The clock continues to scream at you, reminding you that time is limited, and you must keep moving forward. You notice a door to the east, and you know that you must explore this room before moving on. As you take a step forward, you feel a sharp pain in your head. Its like a bolt of lightning, and you feel yourself losing control of your body. You stumble and fall to the ground, writhing in agony. As the pain subsides, you hear a voice in your head. Its not your own voice, but a voice that seems to be coming from somewhere else. It tells you that you are not worthy of escaping this place, that your sins are too great, and that you are doomed to suffer for eternity. You try to fight the voice, to push it out of your mind, but its like a parasite that has latched onto you. The clock continues to scream at you, the sound becoming more and more urgent. You feel like youre running out of time, that death is imminent. The voice in your head becomes louder and more insistent, telling you that you should just give up, that its pointless to keep fighting. You feel a sense of despair washing over you, and you wonder if you will ever be able to escape this mental prison. Suddenly, the door to the east opens, and you see a blinding light. You know that you must move towards the light if you want to survive, but you also know that the voice in your head is right. Youre not worthy of escaping, youve made too many mistakes, and this is your punishment. You move towards the light, the clock screaming in your ear, and you feel yourself slipping away. You feel the seconds ticking by, and you know that death is coming. You feel a sense of regret, of all the things you could have done differently, of all the people youve hurt. You wonder if you will ever have a chance to make things right. And then everything goes black.',
        'items': [],
        'exits': {'death': 'entrance'}
    },

    'north6east4': {
        'description': 'You find yourself in a small room with a pedestal in the center. On the pedestal lies the second key (V), glowing with a strange energy. You pick it up, feeling a sense of relief wash over you. You now have another of the three keys needed to escape this mental prison. As you turn to leave the room, you hear the clicking sound getting louder. The creature has found you, and its more ferocious than ever. you see a sword leaning against the far wall. you grab it and embrace for what is to come next. Victory or death',
        'items': [],
        'exits': {'north': 'north7east4'}
    },

    'north6east5': {
        'description': 'As you explore the room, you notice that there is a hidden door in the corner (XXX). You wonder if it leads to a way out, or if its just another trap. You must make a decision quickly, as the creature is getting closer and closer. With a sense of desperation, you run towards the hidden door.',
        'items': [],
        # add puzzle
        'exits': {'north': 'north7east5', 'hiddendoor': 'north6east4'}
    },


    'north7east1': {
        'description': 'As you step through the door leading east, you find yourself in a small, dimly lit room. You see a locked door in the distance, and you wonder how to open it. You try to examine the lock, but it seems to be unlike any lock you have ever seen before. The clock in the distance starts to scream, reminding you that time is limited, and you start to feel a sense of dread. You start to question your ability to solve this problem, wondering if you have what it takes to continue this journey. The doubts and confusion start to impact your energy, causing you to feel weaker and more vulnerable. You try to push these thoughts aside and focus on the task at hand, but they continue to linger in the back of your mind. As you move closer to the locked door, you feel the weight of the situation bearing down on you. You know that you have to find a way to open this door to progress, and failure is not an option. With each passing moment, your energy starts to drain, and you wonder how much longer you can hold on. But you take a deep breath and remind yourself that you have come too far to give up now. You steel yourself for the challenge ahead, ready to find a way to open the door and continue your quest.  You realize that you dont have the three keys required to open the door. You start to panic, wondering how to find them and what other obstacles lie ahead. The clock continues to scream in the distance, and you feel the weight of the situation bearing down on you. You must find a way to prove your worth and obtain the keys, or else you may be trapped in this twisted, alternate reality forever. you see a stone in the corner and you pick it up. With all your rage you hit the lock... a piercing screamclose through the halls. The lock falls to the ground. In the back of your mind you know you have awoken in it.',
        'items': [],
        'exits': {'east': 'north7east2', 'west': 'north7'}
    },


    'north7east2': {
        'description': '',
        'items': [],
        'exits': {'east': 'north7east3', 'west': 'north7east1'}
    },

    'north7east3': {
        'description': '',
        'items': [],
        'exits': {'east': 'north7east4', 'west': 'north7east2'}
    },

    'north7east4': {
        'description': '',
        'items': [],
        'exits': {'east': 'north7east5', 'west': 'north7east3'}
    },

    'north7east5': {
        'description': '',
        'items': [],
        'exits': {'south': 'north6east5', 'west': 'north7east4'}
    },

    'hiddentreasure': {
        'description': '',
        'items': [],
        'exits': {}
    },

    'freeze': {
        'description': '',


    },

    'playflute': {
        'description': 'You pick up the recorder flute and begin to play a soft melody. The creature seems to relax and begins to sway to the music. As you continue to play, it begins to follow you, its tentacles gently brushing against your skin. You cant help but feel a sense of kinship with this strange, otherworldly being. However, as you continue down the hallway, you realize that the creature is very skittish and skeptical of you. It seems to be testing your intentions, and you know that one wrong move could make it flee. Youre faced with a decision: do you continue to play the flute and try to gain the creatures trust, or do you risk losing its favor by putting the flute away?'
        # create a puzzle.... the Louise armstrong A wonderful night is in the key of F 1, 5,6,4 chord sequence, 72 bpm, 4/4 time
    },

    'treasure': {
        'description': 'Congratulations, you have found the treasure!',
        'items': [],
        'exits': {}
    }
}


# Define functions for handling game logic

def move_player(direction):
    """
    Move the player in the specified direction.
    """
    global player_location

    if direction in labyrinth[player_location]['exits']:
        player_location = labyrinth[player_location]['exits'][direction]
        print(labyrinth[player_location]['description'])
    else:
        print("You can't go that way.")


def get_item(item):
    global player_inventory
    if item in labyrinth[player_location]['items']:
        player_inventory.append(item)
        labyrinth[player_location]['items'].remove(item)
        print(f"You picked up the {item}.")
    else:
        print("There is no such item here.")


def use_item(item):
    global player_inventory
    if item in player_inventory:
        if item == 'torch':
            print("You light the torch and can now see in the dark.")
        elif item == 'key':
            print("You unlock the door.")
            labyrinth['west2']['exits']['west'] = 'treasure'
        elif item == 'sword':
            print("You swing the sword and feel powerful.")
        else:
            print("Nothing happens.")
    else:
        print("You don't have that item.")


def look():
    """
      Print the description of the player's current location, any items in the room, and a puzzle (if applicable).
      """
    print(labyrinth[player_location]['description'])

    if labyrinth[player_location]['items']:
        print("You see the following items:")
        for item in labyrinth[player_location]['items']:
            print(f"- {item}")
    else:
        print("There are no items here.")


def fight():
    """
    Have the player fight the enemy until one passes out.
    """
    playerPoints = 15
    guardPoints = 8

    print("A vile looking guard appears!")

    while playerPoints > 0 or guardPoints > 0:
        # player chooses heavy or light attack
        print("What would you like to do? Heavy or Light attack?")
        attack = input("(heavy/light) > ")

        if attack.lower() == "heavy":  # if attack is heavy, it deals more damage but is less likely to hit
            playerChance = random.randrange(1, 10)
            # players attack hits
            if playerChance > 7:
                playerDamage = random.randrange(4, 8)
                print(
                    f"Your heavy attack hits! You deal {playerDamage} points of damage!")
                guardPoints = guardPoints - playerDamage

                # guard attacks after player hits
                guardChance = random.randrange(1, 10)
                if guardChance > 7:  # guard's attack hits
                    guardDamage = random.randrange(1, 5)
                    print(
                        f"The guard hits you! He deals {guardDamage} points of damage!")
                    playerPoints = playerPoints - guardDamage
                # guards attack misses
                else:
                    print("The guard swings and misses you! No damage taken!")
            # player's attack misses
            else:
                print("You attack the guard but he dodges! No damage delt!")
                # guard attacks player after they miss
                guardChance = random.randrange(1, 10)
                if guardChance > 7:  # guards attack hits
                    guardDamage = random.randrange(1, 5)
                    print(
                        f"The guard hits you! He deals {guardDamage} points of damage!")
                    playerPoints = playerPoints - guardDamage
                # guard misses
                else:
                    print("The guard swings and misses you! No damage taken!")

        elif attack.lower() == "light":  # player chooses light attack, less damage but higher probability of hitting
            playerChance = random.randrange(1, 10)
            # player hits on light attack
            if playerChance > 4:
                playerDamage = random.randrange(1, 5)
                print(
                    f"Your heavy attack hits! You deal {playerDamage} points of damage!")

                # guard attacks after being hit
                guardChance = random.randrange(1, 10)
                if guardChance > 7:
                    guardDamage = random.randrange(1, 5)
                    print(
                        f"The guard hits you! He deals {guardDamage} points of damage!")
                # guard misses
                else:
                    print("The guard swings and misses you! No damage taken!")
            # players light attack misses
            else:
                print("You attack the guard but he dodges! No damage delt!")
                # guard attacks after player's attack misses
                guardChance = random.randrange(1, 10)
                # guard hits the player
                if guardChance > 7:
                    guardDamage = random.randrange(1, 5)
                    print(
                        f"The guard hits you! He deals {guardDamage} points of damage!")
                # guard misses
                else:
                    print("The guard swings and misses you! No damage taken!")
        else:
            print("You must choose heavy or light attack.")

    if guardPoints == 0:
        print("The guard stumbles backwards and collapses in a heap on the floor. He is defeated.")
        return True
    elif playerPoints == 0:
        print("The guards last attack leaves you feeling weak...trying to keep your balance...eyes getting heavy...hard to breathe.......")
        return False


items = ['key', 'sword', 'torch']

if player_location == 'north4':
    print("Here's a puzzle for you: What has four legs in the morning, two legs in the afternoon, and three legs in the evening?")
    answer = input("Your answer: ")
    while answer.lower() != 'man':
        print("Incorrect. Please try again.")
        quit = input("Do you want to quit? (yes/no): ")
        if quit.lower() == 'yes':
            break
        answer = input("Your answer: ")
    else:
        print("Correct! You may proceed.")
        item = random.choice(items)
        print(f"You have received a {item}.")
elif player_location == 'treasure':
    print("Congratulations! You made it to the treasure room and won the game!")
elif player_location == 'north3':
    print("Here's a puzzle for you: I am always hungry, I must always be fed. The finger I touch will soon turn red. What am I?")
    answer = input("Your answer: ")
    while answer.lower() != 'fire':
        print("Incorrect. Please try again.")
        quit = input("Do you want to quit? (yes/no): ")
        if quit.lower() == 'yes':
            break
        answer = input("Your answer: ")
    else:
        print("Correct! You may proceed.")
        item = random.choice(items)
        print(f"You have received a {item}.")
elif player_location == 'west3':
    print("Here's a puzzle for you: The more you take, the more you leave behind. What am I?")
    answer = input("Your answer: ")
    while answer.lower() != 'footsteps':
        print("Incorrect. Please try again.")
        quit = input("Do you want to quit? (yes/no): ")
        if quit.lower() == 'yes':
            break
        answer = input("Your answer: ")
    else:
        print("Correct! You may proceed.")
        item = random.choice(items)
        print(f"You have received a {item}.")
else:
    print("There are no puzzles to solve here.")

# Define the player's starting location and inventory
player_location = 'entrance'
player_inventory = ['map']

while True:
    # Print available commands    
    print("\nAvailable commands:")
    print("- go [direction]")
    print("- get [item]")
    print("- use [item]")
    print("- look")
    print("- quit")

    # Get player input    
    command = input("> ").lower().split()

    # Handle different commands    
    if command[0] == 'go':
        move_player(command[1])
        if player_location == labyrinth['north2east5'] or player_location == labyrinth['north5east2'] or player_location == labyrinth['north7east4'] or player_location == labyrinth['north3west3'] or player_location == labyrinth['north1']:
            if fight() == False:
                player_location = labyrinth['entrance']
                print(labyrinth[player_location]['description'])
    elif command[0] == 'get':
        get_item(command[1])
    elif command[0] == 'use':
        use_item(command[1])
    elif command[0] == 'look':
        look()
    elif command[0] == 'quit':
        break  # Exit the loop    
    else:
        print("Invalid command.")
