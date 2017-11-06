import tkinter
from tkinter import *
import random

#http://stackoverflow.com/questions/35226903/python-3-5-1-reading-from-a-file
#http://stackoverflow.com/questions/5387208/convert-a-string-to-an-array

#noun wordlist
nwordlist= '''Animism, Arctic, Array, Autumn Awareness Beauty Bees Boulder Brook Butte Butterfly Buzz Cliff, Climate, Clouds, Color Cosmography, Crater, Commercial, Commune, Conifer, Conservation, Commercial, Commune, Conifer, Conservation, Current Desert Earthquake Eclipse  Environment, Erosion, Escarpment Esker, Evergreen Fall Farming Flood, Fog, Foliage, Forest, Glacier Growth Habitat, Hail Hibernate, Horizon, Hurricane Iceberg, Imitation Land form, Leaves, Logging Magnificence Marine, Massif, Meteor Mimesis, Moon, Mountains, Mushroom Nature Nurture Peaks, Pinnacle, Planet, Pollutant, Prairie, Predator, Preservation Protection Range Representation Representation Resources Ridge, River, Rock Sanctuary Season, Sediment Shelter, Shore Smells
Snow, Solar Sounds Spring Stream Tarn Terrain Tsunami Value Variety Vista, Volcano Warmth, Weather, Wildlife, Winter flower, stem, petal, grass, tree, evergreen, pine, oak, grove, orchard, fruit, bird, sun, moon, sunshine, butterfly, pollen, rabbit, squirrel, leaf, fur, prey, smell, feel, live die, life, death, soil, wind, dirt, parasite, moss, fern, winter, spring, fall, heat, cold, garden, bloom, burst, compost '''
nwordlist=nwordlist.lower()
nwordlist=nwordlist.replace(',',' ')
nwordlist=nwordlist.split()

#adjective wordlist
awordlist= '''Abundant, Aquatic, Awesome, Barren,, Biodegradable,, Bountiful, Brilliant,, Buoyancy,,,, Celestial, Coastal,, Combustible, Conspicuous, Contiguous,,  Crucial,, Deft,, Destructive, Disposable, Dynamic,, Earthy,, Ecological, Efficient, Electrifying, Endangered, Endemic, Enigmatic,, Exclusive,, Fallow, , Fertile, Fibrous, Fierce, , Gorgeous, Grassland, Gravity,, Gusty, , Healthy, , Hygienic, , Indigenous, Innate, Intense, Intimate, Magical,, Magnificent, , Migratory, , Nascent, Native, Natural,, Neglected, Parasitic, Passionate, Peaceful Popular, , Pristine, Productive, Radioactive,, Renewable, , Reproductive, Reserve, Resilient, , Restorative, , Rotting, Safe, Sane, Scenic, Serene, Serenity, Soluble,, Spatial, Splendid, , Staunch, , Stunning, Taint, , Temperate,, Toxic, Tropical, , Typical, Ultimate, Undeveloped, Unique, Uplifting, Uproot,,, Versatile, Vigilant, Visible,, Vulnerable, , Worldwide, , fresh, enjoyable,, devoid, colorful, anew, alive, active, opulent, blissful, beautiful, awakening, blooming, bright, breezy, blossoming, blue, budding, cheerful, changing, clean, crisp, delightful, enjoyable, floral, fertile, fragrant, grassy, gentle, fresh, free, healthy, green, happy, heavenly, joyful, light, melting, lush, lovely, lively, new, peaceful, pretty, outdoor, pure, rainy, relaxing, refreshing, seasonal, soft, special, sunlit, sweet, sunny, verdant, tender, warm, vibrant, wooded, dense, expansive, elegant, fascinating, vivid, quaint
'''
awordlist=awordlist.lower()
awordlist=awordlist.replace(',',' ')
awordlist=awordlist.split()
    
#http://stackoverflow.com/questions/33990697/python-word-count-of-text-file

text = '''
That thing that we call poetry -
when asked where it began,
I’d say it started beautifully
before the dawn of man!
a
It glistened on the oceans
before man came to be.
It blossomed on the grassy cliffs
that met the first great sea.

It glittered in the moon and stars
and beamed on earth below
in meadows where bright flowers danced
and on the pristine snow.

It sparkled on the lakes and streams,
and when man came along,
he took sweet words that flowed to him
and turned them into song.

This was how it always was
before we knew of time.
The poet who begot us all
made it to be sublime.

Poetry has now evolved,
and as with many things,
there are many kinds.  . .  but I
still like it when it sings!

//

There is a stillness in this frigid night
How peaceful is a planet that glimmers white
where frost and moonlight weave a silver glaze
and sillhouetted trees are black as ink 
Where the only sign of life are whiffs of breath

Let me stand transfixed beneath the sky, 
to rest my mind with reverent eyes
Upon the glorious silence of the world 
Upon these strange and unfamiliar hills
then feel the night's aurora soothe my soul
 
Winter has buried our world in alabaster white
Familiar landmarks wear a cloak of new disguise
Yet still the same are scattered thorny lights
Splattered wildly in the blackness of a sky
Winter has polished up the stars against the dark
Brilliant, new, until their points are thistle sharp

How peaceful is a planet so glimmering white
To stand in voiceless wonder and gaze
Do not speak, the crystal world would shatter
Too fragile to bear the weight of words

//

This seasoned evening
sported a full faced 
Orange Kool-Aid moon.

Fully aware it was a marvel
it shot me an arrogant wink.

Not once but twice.

I think i heard it laugh.

It certainly flashed me an impish smile.
Not much different than my own.

No camera could ever capture
a moment this precious.

This needed,
words-
the heart of my imagination.

I stepped inside.

Pen in hand,
iPad at my right side,
laptop in front of me,
desktop computer behind me,
electric typewriter on my left side
I was ready.

I only hoped I would be able
to express in words what 
I had experienced.

I penned this.

This seasoned evening
sported a full faced 
Orange Kool Aid moon.

Fully aware it was a marvel
it shot me an arrogant wink.

Not once but twice.

I think i heard it laugh.

It certainly flashed me an impish smile.
Not much different than my own.

//


September, beautiful month of my birth, is nigh, but I cannot feel glad."

September, drifting in with glow of moon,
you stifle Summer’s ardor. . . and she grieves.
In guise of fire, the Fall comes all too soon.

Your breath grows cool.  You’ll blow and loosen leaves.
The hills and woodlands will reflect new hues.
You stifle Summer’s ardor. . . and she grieves.

In Autumn’s chill, the colors are a ruse.
For as you pass, the trees are set ablaze.
The hills and woodlands then reflect new hues.

Though warmth may linger through your final days,
old Sun is waning, yet he still seems strong!
For as you pass, the trees are set ablaze.

September, you’re a melancholy song.
Though time be short, you paint a brilliant dusk!
Old sun is waning, yet he still seems strong.

October looms. . . Your ending will be brusque.
September, drifting in with glow of moon,
though time be short, you paint a brilliant dusk.
In guise of fire, the Fall comes all too soon.

//

Palm trees are swaying island style
Within the gentle trade wind's flow,
As Egrets glide on salty air—
Then land where verdant grasses grow.

Breathe in sweet scents of tuberose
And let fine mist caress your face,
Dive deep into aqua waters—
Become enchanted with this place.

Let your eyes consume the beauty,
Let rhythmic music soothe your mind.
You'll feel the aloha spirit—
A kinder people you won't find.

Go hiking in hillside forests,
There are no bears or snakes that hide,
Just waterfalls you'll find waiting,
That flow toward the ocean side.

In the distance whales are breaching,
Humpbacks with little calves in tow.
They share waters with the dolphins,
And green sea turtles down below.

Can you hear paradise calling?
Whispering your name at sunrise,
To later bask on pearly sands.
Swaying hula hips at moonrise,

Coaxing you to join in the dance.
Exotic Mai Tai in your hands,
Sweet flower leis caress your neck,
Come investigate our islands,

And board on wild waves at surfside,
Cast your cold and cares to the breeze.
Sailing out on sunset cruises—
Take homeward bound warm memories.

//

Nature’s wonderful garden in display
display of autumn colours in array
array of beauty to share in delight
delight of birds in a picturesque sight.
Sight of swans as they fly above the ground
ground that is covered by leafs as if gowned
gowned by a blanket of colourful hue
hue of earth moistened by a misty dew.
Dew that reflects sunlights shimmering light
light that wakes up into a morning bright
Bright is the dawn as a new day ascends
ascends to where the earth and heaven blends.
Nature and seasons in a divine bliss
bliss of life and beauty to reminisce.

//

There was a time when meadow, grove, and stream, 
The earth, and every common sight
                 To me did seem
            Apparelled in celestial light,
The glory and the freshness of a dream.
It is not now as it hath been of yore;—
             Turn wheresoe’er I may,
              By night or day,
The things which I have seen I now can see no more.

            The rainbow comes and goes, 
            And lovely is the rose; 
            The moon doth with delight
     Look round her when the heavens are bare;
            Waters on a starry night
            Are beautiful and fair;
     The sunshine is a glorious birth;
     But yet I know, where’er I go,
That there hath past away a glory from the earth.

Now, while the birds thus sing a joyous song,
     And while the young lambs bound
            As to the tabor’s sound,
To me alone there came a thought of grief:
A timely utterance gave that thought relief, 
            And I again am strong.
The cataracts blow their trumpets from the steep,—
No more shall grief of mine the season wrong:
I hear the echoes through the mountains throng.
The winds come to me from the fields of sleep, 
            And all the earth is gay;
                Land and sea
     Give themselves up to jollity,
            And with the heart of May
     Doth every beast keep holiday;—
                Thou child of joy,
Shout round me, let me hear thy shouts, thou happy 
        Shepherd-boy!
				
Ye blesséd Creatures, I have heard the call 
     Ye to each other make; I see
The heavens laugh with you in your jubilee; 
     My heart is at your festival,
       My head hath its coronal,
The fulness of your bliss, I feel—I feel it all.
         O evil day! if I were sullen 
         While Earth herself is adorning
              This sweet May-morning;
         And the children are culling
              On every side
         In a thousand valleys far and wide
         Fresh flowers; while the sun shines warm, 
And the babe leaps up on his mother’s arm:—
         I hear, I hear, with joy I hear!
         —But there’s a tree, of many, one, 
A single field which I have look’d upon, 
Both of them speak of something that is gone:
              The pansy at my feet
              Doth the same tale repeat:
Whither is fled the visionary gleam? 
Where is it now, the glory and the dream?

Our birth is but a sleep and a forgetting; 
The Soul that rises with us, our life’s Star,
          Hath had elsewhere its setting
               And cometh from afar;
          Not in entire forgetfulness,
          And not in utter nakedness,
But trailing clouds of glory do we come 
               From God, who is our home:
Heaven lies about us in our infancy! 
Shades of the prison-house begin to close
               Upon the growing Boy,
But he beholds the light, and whence it flows, 
               He sees it in his joy;
The Youth, who daily farther from the east 
     Must travel, still is Nature’s priest,
          And by the vision splendid
          Is on his way attended;
At length the Man perceives it die away, 
And fade into the light of common day.

Earth fills her lap with pleasures of her own; 
Yearnings she hath in her own natural kind, 
And, even with something of a mother’s mind,
               And no unworthy aim,
          The homely nurse doth all she can 
To make her foster-child, her inmate, Man,
               Forget the glories he hath known,
And that imperial palace whence he came.

Behold the Child among his new-born blisses,
A six years’ darling of a pigmy size!
See, where ‘mid work of his own hand he lies,
Fretted by sallies of his mother’s kisses,
With light upon him from his father’s eyes!
See, at his feet, some little plan or chart,
Some fragment from his dream of human life,
Shaped by himself with newly-learned art;
          A wedding or a festival, 
          A mourning or a funeral;
               And this hath now his heart,
          And unto this he frames his song:
               Then will he fit his tongue
To dialogues of business, love, or strife; 
          But it will not be long 
          Ere this be thrown aside, 
          And with new joy and pride
The little actor cons another part;
Filling from time to time his ‘humorous stage’
With all the Persons, down to palsied Age,
That life brings with her in her equipage; 
          As if his whole vocation
          Were endless imitation.

Thou, whose exterior semblance doth belie 
          Thy soul’s immensity;
Thou best philosopher, who yet dost keep
Thy heritage, thou eye among the blind,
That, deaf and silent, read’st the eternal deep,
Haunted for ever by the eternal Mind,—
          Mighty Prophet! Seer blest!
          On whom those truths rest
Which we are toiling all our lives to find,
In darkness lost, the darkness of the grave;
Thou, over whom thy Immortality
Broods like the day, a master o’er a slave,
A Presence which is not to be put by; 
          To whom the grave
Is but a lonely bed, without the sense of sight
Of day or the warm light,
A place of thoughts where we in waiting lie;
Thou little child, yet glorious in the might
Of heaven-born freedom on thy being’s height,
Why with such earnest pains dost thou provoke
The years to bring the inevitable yoke,
Thus blindly with thy blessedness at strife?
Full soon thy soul shall have her earthly freight,
And custom lie upon thee with a weight
Heavy as frost, and deep almost as life!
          0 joy! that in our embers
          Is something that doth live,
          That Nature yet remembers
          What was so fugitive!
The thought of our past years in me doth breed
Perpetual benediction: not indeed
For that which is most worthy to be blest,
Delight and liberty, the simple creed
Of Childhood, whether busy or at rest,
With new-fledged hope still fluttering in his breast:—
          —Not for these I raise
          The song of thanks and praise;
     But for those obstinate questionings
     Of sense and outward things,
     Fallings from us, vanishings,
     Blank misgivings of a creature
Moving about in worlds not realized, 
High instincts, before which our mortal nature 
Did tremble like a guilty thing surprised:
     But for those first affections,
     Those shadowy recollections,
          Which, be they what they may,
Are yet the fountain-light of all our day, 
Are yet a master-light of all our seeing;
     Uphold us—cherish—and have power to make 
Our noisy years seem moments in the being 
Of the eternal Silence: truths that wake,
               To perish never;
Which neither listlessness, nor mad endeavour,
               Nor man nor boy,
Nor all that is at enmity with joy,
Can utterly abolish or destroy!
   Hence, in a season of calm weather
          Though inland far we be,
Our souls have sight of that immortal sea
               Which brought us hither;
          Can in a moment travel thither—
And see the children sport upon the shore, 
And hear the mighty waters rolling evermore.

Then, sing, ye birds, sing, sing a joyous song!
          And let the young lambs bound
          As to the tabor’s sound!
     We, in thought, will join your throng, 
          Ye that pipe and ye that play, 
          Ye that through your hearts to-day 
          Feel the gladness of the May!
What though the radiance which was once so bright 
Be now for ever taken from my sight,
     Though nothing can bring back the hour 
Of splendour in the grass, of glory in the flower;
          We will grieve not, rather find
          Strength in what remains behind;
          In the primal sympathy
          Which having been must ever be;
          In the soothing thoughts that spring
          Out of human suffering;
          In the faith that looks through death, 
In years that bring the philosophic mind.

And 0, ye Fountains, Meadows, Hills, and Groves,
Forebode not any severing of our loves!
Yet in my heart of hearts I feel your might;
I only have relinquish’d one delight
To live beneath your more habitual sway;
I love the brooks which down their channels fret
Even more than when I tripp’d lightly as they;
The innocent brightness of a new-born day
               Is lovely yet;
The clouds that gather round the setting sun
Do take a sober colouring from an eye
That hath kept watch o’er man’s mortality; 
Another race hath been, and other palms are won.
   Thanks to the human heart by which we live,
   Thanks to its tenderness, its joys, and fears,
   To me the meanest flower that blows can give
   Thoughts that do often lie too deep for tears.

//

The birches stand in their beggar’s row:
Each poor tree
Has had its wrists nearly
Torn from the clear sleeves of bone,
These icy trees
Are hanging by their thumbs
Under a sun
That will begin to heal them soon,
Each will climb out
Of its own blue, oval mouth;
The river groans,
Two birds call out from the woods

And a fox crosses through snow
Down a hill; then, he runs, 
He has overcome something white
Beside a white bush, he shakes
It twice, and as he turns
For the woods, the blood in the snow

Looks like the red fox,
At a distance, running down the hill:
A white rabbit in his mouth killed
By the fox in snow
Is killed over and over as just
Two colors, now, on a winter hill:

Two colors! Red and white. A barber’s bowl!
Two colors like the peppers
In the windows
Of the town below the hill. Smoke comes
From the chimneys. Everything is still.

Ice in the river begins to move,
And a boy in a red shirt who woke
A moment ago
Watches from his window
The street where an ox
Who’s broken out of his hut
Stands in the fresh snow
Staring cross-eyed at the boy
Who smiles and looks out
Across the roof to the hill;
And the sun is reaching down
Into the woods

Where the smoky red fox still
Eats his kill. Two colors.
Just two colors!
A sunrise. The snow.

//


I leant upon a coppice gate 
    When Frost was spectre-gray,
And Winter’s dregs made desolate
    The weakening eye of day.
The tangled bine-stems scored the sky
    Like strings of broken lyres,
And all mankind that haunted nigh
    Had sought their household fires. 

The land’s sharp features seemed to be
    The Century’s corpse outleant,
His crypt the cloudy canopy,
    The wind his death-lament.
The ancient pulse of germ and birth
    Was shrunken hard and dry,
And every spirit upon earth
    Seemed fervourless as I.

At once a voice arose among
    The bleak twigs overhead
In a full-hearted evensong
    Of joy illimited;
An aged thrush, frail, gaunt, and small,
    In blast-beruffled plume,
Had chosen thus to fling his soul
    Upon the growing gloom.

So little cause for carolings
    Of such ecstatic sound
Was written on terrestrial things
    Afar or nigh around,
That I could think there trembled through
    His happy good-night air
Some blessed Hope, whereof he knew
    And I was unaware.



A silica odor, dust walks through a fresh desert night
Cool air beneath and above the sea
A warm furnace smell, I don’t understand
Intricate to rise and receive without knowing
Up ahead in a virtue distance
A mysterious poisonous effluvium light-     
My face feels like a leaf'
My sun holds up its own pendulum rods
Inflammation comes and settles in for the night,
There it stands in a pertinacious manner, with quality
I resurrect this air created from madness, all over again
Twilight, rain stranger than strange
Visions, pursue my path into an infested dark pasture
"From the red Heaven I fell into the waters of a cobalt Hell"

Perhaps this venerable moment, will pass slower than slow
PERHAPS NOT!
If I accept, and then decline
Would this balance the precocious state I live in?
How about when wrong directions follow my promiscuous ways 
Is my conglomeration of ideas, no longer safe?	
When I no longer value the values of the young
Will I sleep at the mercy of his ancient heart
They're the voices give and take from our health

Today, those soft, perfect eyes are calling from far away,
Ashes high, vapors and infection welding me
The bright skies swallow every thin silver line,
Where the clouds sit somehow~ in bacteria
UNITY! 
YES UNITY! Fantabulously-fantastic!
Always, wanting more than love can touch

We are living' it up with no alibis!
A way to be and not to BE!
The champagne leaves their cup
Awaken in a life, disturbed ~ NOW INTERRUPT!
Only in this world, lava will reach her lips
Prisoners and doers; 
All night…. Too late for a treatment
Lungs, decaying, evil rats
Direction, affection, ending all the inhalation

Pneumonoultramicroscopicsilicovolcanoconiosis, 
Running through my lungs,

The powdery snow gloves the fingers 
of maple forest, protecting barren bark 
with the expectation of rose tipped bloom.

A meeting point between pristine
innocence and the veiled promise of spring
ripening. Each trunk and limb mirrors 

the action of man. Reaching, arching, 
swaying, creating aisles of church-like splendor, 
a sacrament where the virginal may walk

toward communion with their God. Inward 
toward the birth of faith and outward toward 
the wedgwood sky in celestial sight.

Palm trees are swaying island style
Within the gentle trade wind's flow,
As Egrets glide on salty air—
Then land where verdant grasses grow.

Breathe in sweet scents of tuberose
And let fine mist caress your face,
Dive deep into aqua waters—
Become enchanted with this place.

Let your eyes consume the beauty,
Let rhythmic music soothe your mind.
You'll feel the aloha spirit—
A kinder people you won't find.

Go hiking in hillside forests,
There are no bears or snakes that hide,
Just waterfalls you'll find waiting,
That flow toward the ocean side.

In the distance whales are breaching,
Humpbacks with little calves in tow.
They share waters with the dolphins,
And green sea turtles down below.

Can you hear paradise calling?
Whispering your name at sunrise,
To later bask on pearly sands.
Swaying hula hips at moonrise,

Coaxing you to join in the dance.
Exotic Mai Tai in your hands,
Sweet flower leis caress your neck,
Come investigate our islands,

And board on wild waves at surfside,
Cast your cold and cares to the breeze.
Sailing out on sunset cruises—
Take homeward bound warm memories.

One leaf fell from a tall, tall tree
and subtly kissed gnarled roots beneath;
a lover’s kiss below sunned-sheath 
of greenest leaves, a jubilee.  

One spiraling leaf brought playful mirth
to sullen earth of trodden dirt.
A flight of hopeful shades of spring,
for hard, hard ground, an offering

One leaf dressed in a sparkling jade
glided with grace to green grass blades    
and rested near a bubbling brook,
then waited for warm breeze that shook
its flirty skirt on green, green glade.   

An arc of bright green canopy
warmed my heart in bluest mood, 
and one leaf blew a kiss from you.
It twirled and pranced and floated by,
then with a touch it came to lie 
green in my hand, a dear surprise. 

Like emerald hills of Irish tales, 
I marveled at how one leaf sailed
green In my hand that blue, blue day,
a kiss from you on Patty’s Day -
The gray clouds parted shining green, 
a beauty like I’d never seen.

I see the wrinkles in your suntanned brow,
You carried burdens then; you see them now.
You’ve heard the cries your people who in pain,
Have shed their tears two hundred years like rain. 

Your sad brown eyes, reflecting now the sky
I see the wings of eagles flying by
Beside you stands an Appaloosa mare
Her spirit one with you now over there.

You hear the drums, they bid you to come near,
Your spirit drawn the beats they ring so clear.
Song like prayers are chanted through the night,
Calling you come, and help them end their plight.  

You’ve heard sad cries and now stand at their side,
You join the prayers with both arms open wide,
United spirits sing until the dawn,
When in the fire’s flames a golden fawn.

Remembering a smile crosses your face,
When tribes were one with Mother Nature’s grace.
The lakes and streams flowing with waters clear,
Flow sadly now, the planet lives in fear.

The weightless feathers that adorn your head
Your tribes grey future weighed you down instead.
Now breathing deep you smell the winds of change
While here on earth your people rearrange.


Floating down with grace and ease
Carried off by the Autumn breeze
Rich in hues of orange and red
Landing in the flower bed

What once was buzzing full of life
Now succumbs to the pruning knife
Staring up at the wilted rose
Another season comes to close

Looking for memories of this day
Not forgetting her fun filled stay
Lying amongst the rocks and sticks
I'm the one the little girl picks

Hurries home with the one she took
Placing it in her poetry book

My garden is such a colourful sight,
with pretty roses and scented sweet peas.
An abundance of blooms, what pure delight!

Beautiful butterflies gently alight
on flowers dancing on the summer breeze.
My garden is such a colourful sight

Sweet night scented stocks abloom at midnight
their aroma is always sure to please.
An abundance of blooms, what pure delight!

Carnations in purple, scarlet and white
are visited by busy bumble bees.
My garden is such a colourful sight

A haven for birds I watch them in flight
they alight on peach blossom from the trees.
An abundance of blooms, what pure delight!

Pretty pansies smile in clay pots so bright
I love beautiful flowers such as these.
My garden is such a colourful sight
An abundance of blooms, what pure delight!

To appreciate planet Earth
start with its snow capped mountains,
where sunbeams morph crystals of ice
into gems of glistening light.

Witness clouds traverse its skies
floating on a vista of blue,
or a setting sun smear scarlet
onto puffs of marshmallow white.

See jungles at its equator,  
create a sash of vibrant green,
and burnt sands ripple its deserts 
with shifting dunes of tans and creams.

See its leafy forests change from
deciduous to evergreen,
and tundra pitted with blue lakes
fade to stretches of virgin snow.

Watch volcanoes erupt in flame
spuing plumes of ebony smoke,
lava bleeding from gaping wounds
while giving birth to molten earth.

See azure and aquamarine
waves crested with white foamy froth,  
or tilted poles capped in ice
sparkling like crystalline jewels.

View it from afar as it spins
in the vacuum of space, like
a phantasmagorical
glossy cerulean marble.


The sky is one gigantic bowl of pink
turned upside down,
spilling soft rosy petals that peeked out
from beneath snow white billowed clouds
till - fully blossomed - they burst out.

Growing radiant at the edge of twilight,
they’ve scattered as rubescent streaks falling,
lush and luminescent, as we watch in solitude.
No parade this evening - just you and I aglow,
wishing for an eternity to be like this:
so splendidly in love. . . 
in the pink.

 If I could sing a song,
   It wouldn't be just any song.
   I would sing a song about a fish
   A fish who is not a fish, but a whale
   Not just any whale, A Narwhal

This night I'll sing a short song of a whale
Dancing under the moonlight dusk
Swimming with ivory tusk, underwater musk
Rising to the morning glory in the sky
Communicating with the waves
Squealing around, 
Trilling and clicking supersonic sounds

   If I could tell you a tale
   It wouldn't be just any tale
   I would tell you a tale of a fish
   A fish who is not a fish, but a whale
   Not just any whale, A Narwhal

Grayish brown, 
White freckled belly crown
Elusive and mysterious
Without the Arctic water, I'll get delirious
A rare whale, with a tooth for a hoot
Enjoying shrimp, squid, and fish food
Taking care of the young, 
I swim in pods all day long
I' stay away from what consumes my cod
Polar bears, orca whales and native spear
My greatest fear and nightmares.

   If I could share some words
   It wouldn't be just any words.
   I would share some words about a fish
   A fish who is not a fish, but a whale
   Not just any whale, A Narwhal

Deep, down the ocean odyssey
My beliefs and skin peel easily 
With a tear, I drown
When called "The Underwater Unicorn"
My words are naught more than a sad song I sing
A tale of a whale not just any whale, A Narwhal
The next time you go out to sea
Looking for blubber and ivory
Please don't look at me!
For I am just a Narwhal 
And, I belong to the sea

The hem of nature floats as seasons blend
with winter’s lasting days now lost and spent,
as endless summer frozen shadows mend
without the youthful feelings of lament.
In distant land where future dreams ascend
beneath the southern sky of golden light,
by heaven‘s gift a love of life transcends
on landscapes tranquil beauty’s kind delight.
As graceful night unfolds its cast on day
with morning dew of many coloured hues,
and sunrise magic cuddles shoreline's bay,
the warmth of life another love renews.

With fervor I adore the seasons grace,
as nature's peaceful fairness I embrace.

Dear Quintain, how beautiful you are,
allowing us to paint the spacious sea or sky, 
landscapes, or nights’ celestial bodies beckoning from afar.
Even when my quill is running dry,
with you along, my thoughts are sure to fly!

For all I need to do
is let you slip inside, then nestle in my brain.
The pattern of rhyme required by you
is not too difficult; here I will remain
content to write with you, dear Quintain.

Your English form, so lovely, does not ask
that we adhere to meter even though
I want to dance your lines as I bask
in your sweet simple charms, and lo!
My quill has filled; my lines now start to flow!

I’ll keep on going for two stanzas more
because I wish to sing
your praises! My mind is like a shore
upon which you are tumbling, glistening!
A sea of inspiration you bring.

Continue on - through poets - bringing words
that paint our world, entreating all to see
God’s gifts or to enjoy the singing birds,
taste clear mountain springs, and smell the salty sea.
Continue, dear Quintain, enrapturing me.

With the turning of the green
the fevered hues engulf my soul
rich radiant reds glistening in the sun
as my heart gleams with memories
of the solemn words that fall from
your angelic lips.
The ornate orange and dynamic yellows
come to life
like those sparkling flecks dancing
inside your autumn eyes. Oh my heart
my heart, rest my heart.
Breathless the breeze blows a subtle scent
of sweets from the pink flowing Amaryllis.
Blow sweet breeze blow  off into the night
and on your wings I plant my kiss. A loving kiss
filled with the finest fruits of my harvest like the
finest bottle of red served on the terrace overlooking
the Grande Canal in Venice under a moonlit sky.
Blow sweet breeze blow and onto her veranda swirl
swirl gently into her palatial palace and wrap my love
firmly upon her waiting cheek.

Trees wear a gown of bright emerald green
Where birds are nesting in branches up high
Parents shield fledglings so they can’t be seen
Until they can spread their new wings and fly

Daffodils dance in the warm zephyr breeze
Bees buzz seeking out these pretty flowers
Yellow pollen doesn't make the bees sneeze!
They will pollinate blooms for many hours

Young lambs gamboling around in the fields
Birds fly high in the sky of azure blue
I love the spring season where nature yields
Our earth’s a stunning place for me and you

Spring brings rejuvenation to our land
The vibrant countryside looks very grand

Whatever, 
what about space and time, 
which came first?

Same question. 
Same answer. 
Space adds formed place 
to time's potentiating and exforming bilateral linear function.

All right, 
so linguistic paradox meets coincidental evolution as co-arising time travel, 
I guess.

About time.

So you say.
And, yang and yin?

Same question.
Yang empowers Time's form
while Yin unfolds as yin-yin nondual co-implicating bipolarity,
bicamerality,
binary form,
all binomial time and co-gravity frequencies,
synergetic natural trend strings and cycles and tipping points,
mutually revolving gravity waves;
double-binding,
like not-not injunctions
and co-arising natural intelligence
as accessible as the nearest regenerating cell,
inductive intuition,
subconscious non-languaged awareness
of integrating communication as cooperative community,
emerging from an enthymematic holding place
of polycultural multisystemic Black Hole dual-dark love,
subconscious being,
co-givenness,
fore-givenness,
mutual subsidiary solidarity
and coredemptive navigation from past stimuli,
pulling, inviting, seducing, branching
toward future's ecojust karmic response,
ecological reconnections from past to future in each present moment,
re-genesis of The Tree of Co-Arising Death and Life,
fear of too-brief time's revelation, revolution,
between death and life and rebirth
yielding both further death and purgation
and further freedom and facility and harmonic diversity
of both species and uniquely ego-centering song;
until we sometimes overheat our climatic landscapes 
with less than fully optimized cooperative function.

Wow!
Was that good for you?
I don't know how many nested climaxes you intended to create there,
but, anyway, 
what about dark and light,
black and white,
dispossession and possession of transparency?

Same question.
Black is white light's full octaved closed-set form
as light is emergent black's informating octave-ergodic dark-dense function.

So is that like a color wheel observation
or some kind of cosmologically universal statement?

Yes.
The ultra-violet spectrum completes time's full octave frequencies,
your human natured atomic picture frame,
the outline of a tree
including the tree's equivalent subterranean understory,
and undervalued root system.
Undervalued by egocentric left-brain dominant culture,
not by right-left bicameral balancers
and health/wealth harmonizers
and permaculturists,
all the way back to shamans noticing naturally seasoned
cycling systems of birth and decomposition
and then new birth again.

You did it again, 
that thing 
when you sound like you're channeling Bucky Fuller
and you start talking about one thing
and then pulling words about some other irrelevant thing,
turning analogical coincidence
into ecological correlates.

Yes.
I suppose that's how language evolved
to iconically place-hold neural memory patterns
of synaptic crisis and aptically benign eco-norms,
structured as DNA fractals,
cycling octave holonic frequency functions.

I'll take a pass on even pretending
connections between DNA's structure  
and revolving articulation of syntax.
How about the chicken and egg?
Which came first?

What's the difference?

I don't know.
It's one of those questions philosophers like to ask.

No.
I mean, what's the difference between a chicken
and its egg?

Well, one has feathers and wings 
and sometimes lays an egg
and the other is sort of oval
and smooth hard-shelled,
and gooey inside.

This chicken you are asking about,
did it lay the egg
you are asking about,
or
did this chicken emerge from the egg
you are asking about?
Or, maybe both, 
at different stages of chicken with egg development?
If so,
then I guess they too evolved coincidentally.
If I may comment off record here,
you keep asking questions about evolutionary production
and consumption cycles,
as if progenitive decomposition,
metamorphic transitions
through self-renewing stages of paradox
were not the reverse face of regeneration,
as if we could have mature plants 
during summer's contenting heat
without cold hibernation 
of winter's dissonant contentiousness,
or any concept of optimized cooperative living
without something we fear as death,
loss of corporate-structured life.

I told you I would only do this interview
if you promised to not critique
our stupid questions.

There is no such thing,
but some are much more perennially
and permaculturally productive than others.

If you say so.
What would be the most insightful question I could ask you
and please go ahead and answer it too.
Save me some trouble.

Why is the duration of your DNA's life potential
measured only with egocentric
"Closed Set Universe" rooted quantitative values?
Because "Open System" inductive/consumptive life-form balance
is only perpetually (not conclusively) defined 
by eco-ionic production of (0) sum binomial root systems, 
double-crossing Eulerian prime relationship spacetime function.
The beginning and end of your DNA string 
appear terminal rather than transitional
if you identify your self as ego,
rather than as your co-operative portion of eco-regenerative consciousness.

OK, well, thank you for that,
I think.
How do you feel about the ground covered so far?
Anything else I should ask?

I wish you would give higher priority
to ecological and feminist justice platforms.

What's the difference
between a feminist agenda
and an ecological platform?

Nice job;
very excellent question.
Which came first
is like asking which is the producer 
and which is the later consumer,
when these functions emerge coincidentally
throughout a life,
a dream,
a generation.


Truth is a feather 
pushed off to the other side.

Truths are a body of feathers
within which our bodies reside.

OK, students of life’s healthiest purposes and meanings,
it’s time to regather, if you would be so kind.

Namaste.

[Silence]

[My EcoTherapist is trying to recall our bicameral minds with ecological bodies.]

[More kinda creepy silence.]

[I wonder if I have time for a cigarette.]

How do you understand “mind” as other than “body”?

[OK, she leads with a dualist assumption
for a session advertised as nondualist,
so the correct answer must be,
I don’t.]

Which, mind or body, do you believe came first,
or do you believe,
as I do,
consciousness and biosystems co-arise nondually?

[I knew it!
Biosystems are self-identifying consciousness-rememory 
DNA-encoded systems, or RNA, if you’re a tree or something green,
from before the time when physical root systems
transubstantiated into metaphysical regenerate root bilateral,
then bipedal, 
then bicamerally balancing,
eco-political systems.
I remember our history of biological evolution co-mentoring sessions,
out on the coral reefs of time’s surfing copresence.]

If mind emerges from reiterative and redundant and resonant neural-cellular development,
in these, and probably other, senses co-arising nondually,
then what do you think could survive of your Ego identity
upon total biosystemic flatline demise of your natural-chemically elementary cellular body?

From where would sensory consciousness and memory emerge?
From when, and for how long?

[Hang on there now. I’m stuck back on the where question, 
which I think should probably default as Nowhere,
Ego emerges from nowhere?
No, no, If dead,
then Ego as sensory consciousness and memory is nowhere
at that time, and on into the future of EarthTribal evolutionary history.
No such phenomenon.
No such experience within continuous Earth-spinning Time.
I think?
But only as long as I dance this Ego-consciousness string
I am]

As your mindbody decomposes,
is this really still your Ego’s story?
In that future time of opportunities for health and relationship
and transactions,
capacities for ongoing communication,
you struggle to face their mortal loss now, projecting forward,
we struggle together to find faith 
these lost opportunities are not your post-critical event
of loss, decay, absence, inevitable physical and mental defeat.

[I don’t even have faith that anyone will think that day
has come even one day too soon.
Nor would I care to invest in such an unwise faith.]

Or,
in the face of this inevitable termination of Ego’s mindbody story,
do you, 
as unfolding conscious memory-string of continuous information,
transform into your nutritionally reiterating responses and contributions
yet reverberating within EarthTribe’s ReGeneration Story?

Is your Ego expanding out toward Earth’s Story?
pregnant pregenetic, nearly timeless Creation Story,
out and yet deeply into this Elder (0)Riginal Intent.

Body memory transforming within ecopolitical truths of post-taoist beauty,
remembering—revolving—rewinding—reweaving
ecologic of Ego/Eco balancing
embryonic bicameral
dipolar cognitive/affective neural emergence
(0) CommonsCentered DNA/RNA code—syntax
healthy reverse development instructions
for normative natural/spiritual
mind/body elational resonant resolutions
giving oneself birth into this body’s time
as giving ourselves freedom
for time’s codependent love of light ourselves.

[My self-image emerges rather far toward the depressive side
of love as ecoconscious light myselves.
Oh, wait, maybe that connection between agape as Basic Attendance,
understory of all those relational dramas, and nonrelational boredoms,
and fears,
and angers,
and….]

Memories,
knowledge,
thoughts,
comprehension,
dissonance and dismay,
feelings of elation and relation,
anticipation,
innocence,
ignorance,
love and hate,
anger and fear,
all Ego’s products,
as Ego, in turn, is produced
by unfolding DNA instructions
within a nurturing DNA-developed warm embryonic pronoic womb
living in this specific time
within  Earth’s evolution of continuing ecosystemic health-consciousness.

[Oh, I get it, health as therapy-consciousness.
Puts a postmillennial twist on post-doctoral medicinal sciences.
Kind of self-serving, though, 
unless all humane-nature is for ecotherapeutic vocations,
in dying as in living,
in living as optimally visible through mortality’s timeless lens.]

What we inherited from Elder wombs of Time’s incarnation
is what Ego becomes
to cherish as responsible authority
rooted within teleologically exegetical historic evidence
unveiling regenerative evolutions as cooperative nested-networks,
and to let go free as a last pay-it-forward gift
to nurture future healthy regenerations of time
bilaterally echoing
fractal-polypathic light,
(0)-TaoWombTime.

[Why do I feel like I could use a bath
more than a cigarette?]

Time,
dualdark
deepdense Ego-Ecohypnotic co-elational learning bright,
white octaving night,
protons merging eco-lateral binomial electronically issuing waves
as Yes! reweaves notnot 
yinyin
WinWin embryonic-yet.

[I’m wondering if there is something in Taoist water
that regenerates this wu wei balance
spinning through my bicamerally revolving mind
as body?]

Could you become as curious about other’s Ego development stories
as you have obsessed about your own?

[Wait a minute,
when did I give you the OK to label me as self-obsessed?
Or maybe the balance point here 
invites comparisons between obsessive curiosities,
in which case
perhaps my own Ego health constant revival
does indeed lie most mortally on my failing mind.]

If so,
please note differences
but memorize Earth’s natural systemic similarities,
especially about what we all want our end to say
one day's capacities for love as peace,
about gradually subsiding incapacities of anger Ego losses
and fear of/for future Earth as sacred compost, 
transubstantiating post-climatic residency.

Namaste.

[Namaste.
Oh wait,
was I supposed to write that out loud?]

Stepped inside Bucky's Universal Credit Union today
to ask what could I invest in
with least risk
and greatest potential for self-optimizing return?

He invited me to sit down
to consider cooperative transactions
as our intentional understory
camouflaged within our ecotherapeutic relationships,
like summer's warm sun emerging from winter's cold clouds,
like noon folding out from appositional midnight,
like death enfolding regenerative life,
like life unfolding transmorphic death of Mother's absorbent egg,
like space unfolding time's eternally present 
diastatically emergent 
NOW.

So, here I sit
while economic advisor Fuller
explicates his negative corollary:
sociopathic Win-Lose strategies of domination
and dissonant relationships with oneself
others,
Earth and all her diversely lovely tribes,
is business-as-usual competitive investment
or disinvestment away from: 
cooperative compassion,
ecotherapeutic justice for all,
choosing to live within mutual subsidiarity
and solidarity of purpose.

I was hoping to find and incubate a nest egg
free of unbalanced blemish,
divested of too much Yang empowerment
of competitive Western culture,
Left-brain domination of Earth's Yin-Yin
Win-Win chronic thrival of the integrative fittest,
like permaculturist designs and cooperative lifestyles,
time's yang/yin spirally revolving balancing ergodic act
of thermodynamic and electrogravitational balance,
rather than increasing climatic eruptions within 
and without.

This Universal Credit Union follows Intelligent Cooperative Design,
synergetic,
active mutual-mentoring principles and investment policies,
Bucky responds,
supporting our logical conclusion,
our current ecological outcome,
that Yang-Left brain competitive Win-Lose cultural domination
trends already toward burning,
consuming more of Time's resources,
enspaciating
incarnating a planetary hydraulic temporal crisis.
Our decompositional function, as a species,
has not kept pace with regenerating Earth's Solar Systemic balanced nature.
We "educate" both producers and consumers
about most everything except how to keep these two primal
Yang with Yin flow and form and force functions in balance
as individuals
and families,
neighborhoods and indigenous communities of increasingly siloed,
isolating, 
marginalizing
disrespecting
desacralizing our evolved diversity.

Those with eyes and ears to see and hear eco-centrically,
join this Universal Credit Union.
Those who see and hear best,
most ecologically,
remain most rationally
and mindfully-conscious
and cooperative economists;
rather far afield from Dominatrix 
short-term stock holder incorporation,
incarnation,
enculturation about ownership without commitment,
passive-aggressive possession and dispossession.

I would very much like to invest in this natural resource we call time.
To invest in working with time,
is to divest of working against time.
To struggle with time together,
is to divest of struggling against time.
To invest in designing with time's natural seasons and days 
and consumer-producer balancing ways,
is to divest of designing against time's intrinsic
permacultural nature.

Our Universal Credit Union's self-optimizing ecotherapy
balances dipolar time's negative correlational view
of full Yang as overly dominating and toxic power,
and full Yin as overly chaotic, entropic disynergetic,
disunitarianism;
lack of discernible relationship, 
resonance,
resolution,
regeneration,
redemption,
lack of an on-target balance, 
wu-wei response.

Predicting cooperative economic optimization
follows permacultural design precedent,
balancing four essential natural functions,
each within its dynamic season:
Summer's full production follows new life's energetic consumption,
as winter's decompositional design analysis
follows autumn's falling regenerative seeds.
Ecojustice practice seeds naturally cooperative production 
as ecotherapeutic temporal design and intention
informs future's regeneration of living diversity,
evolution.

This permaculturing credit union actively loves win-win cooperation
with time.
Time's power is not our ultimate shared enemy.
Time reveals its nutritious and/or toxic nature
through our relationships,
our transactions,
our actions together or divisive,
through what we absorb,
consume,
and what we produce,
what we dissonantly or confluently offer
with each communication,
day,
and life.

Given your current assets,
responsibilities,
investments,
vocations,
family,
property and cooperative political and sociotherapeutic values,
and disvalues,
all your confluences and dissonances,
all your positives and negatives,
all your loves and your hates,
all your ego power and your eco-passioned mind,
your win-win gaming assumption
that we are all invested in regenerative life together,
then what do your negative dissonant competitives
teach you about future possibilities for positive confluent cooperatives?

For each human natural system,
whether we sub-optimize with ego-centric awareness,
or synergetically optimize with eco-centric consciousness,
depends on which one we feed most nutritiously.

Never give up.
Always give down stream, whenever possible.
Time's creative right-now interdependent risk,
for freedom and opportunity,
for justice with peace,
is Yang-future as Yin-past karmic eternal presence,
gifting each one forward toward downstream,
while looking out and up stream with gratitude
for all who have come through this DNA string
back to our shared RNA original point of time's awareness,
meaning,
and balancing purpose of synergetic, 
loving life.

We only give downstream, toward our future, 
what and whom we would all hope to receive from upstream's past.
We never give out to a hopeless past;
we always give in to our faithful present.
We never give back our gifts from time's past.
We always give forward 
to cooperatively invest in our shared therapeutic future.

We soar through time's economy together
when we avoid competing to individually fly up and out and apart.


I was listening to Cornell West,
who described our catastrophic tolerance of disvalues for others,
situations we would never tolerate for ourselves,
disvalues like homelessness and hunger,
but also like random violence, 
abuse and neglect,
lack of caring,
as a "conspiracy" of a dominating, oppressive, and competitive culture.

Conspiracy theories make me nervous about the theorist,
but West reassured us that he shares this concern,
yet even with all that concern taken into account,
perhaps this is a conspiracy 
in the same sense that cultural and climate evolutions
always appear, in hindsight, 
as if genius inspired, 
intelligently planned
and spontaneously networked
a magically coincidental outcome.
Positive sometimes,
and sometimes more about this mystery 
of tolerating oppressive and suppressive disvalues for others,
with apparent equanimity,
unaware of any cognitive dissonance,
without active antipathy,
or even passive empathy,
the total absence of compassion,
lack of mindfulness,
lack of consciousness;
unconsciousness.

Our own hypocrisy of self v. other values v. tolerable disvalues
are hypnotic conspiracies?  
Magical miracles?

Yet, conspiracy or not,
if self-contentment is possible
while hypocritically accepting intolerable losses and suffering,
abuse and neglect, for other:
species,
Earth-plus-atmosphere ecosystem,
nations,
cultures,
neighborhoods,
even other family members,
then we sometimes would choose words like
irrational,
rabid,
irresponsible,
lack of appropriate accountability,
lack of capacity for empathy or bonding,
lack of awareness, consciousness,
hateful,
stupid,
mental disease,
sociopathology,
ecopathology,
a hypocritical living death cuts by a thousand ego-feathered knives.

We work this magically competitive hypocrisy with each other,
on each other,
against each other,
and sometimes with each other--
we call that humor.

I do not feel possessed
when my internal ecological voice
tells me that my monocultural competitive economic environment
is over-invested in undervaluing significant dimensions
of who we naturally and cooperatively (permaculturally) are,
our care-giving and loving,
our tenderness and justice-seeking,
our tendency to side with the underdog and the understory,
our endless fascination with root systems and nutritious blossoms,
seasonal development patterns and the weather,
birdsong and surf sounds,
regular breathing and heart-beat rhythms,
blood flow nutritional capacities,
the consumption and production of nutrients
within any paradigm that might come to mind.

I get it that I live in a culture diseducating ourselves
about Darwin's "evolution is the survival of the fittest cooperative relationships"
by simply omitting the last two words;
cultural hypocrisy miraculously conspired through our sins of omission,
more salient than our grace of cooperative inclusion,
because of collective cognitive dissonance
where we need collective cognitive confluence.

Perhaps a more resonant resolution of consciousness
calls us to slow down and decompose our analysis of deviance
as sometimes negative and sometimes positive
but always some of both.

I struggle to hold a heuristic safe-space for positive deviance.
My cognitive dissonance radar 
learns to perceive dissonance itself as having two faces.
In this way
I begin to claim my positive deviant place
in our shared orthodoxy of truth and goodness,
beauty and diverse polycultural integrity,
in our "unitarianism" our synergy (B. Fuller),
our love.
If I am challenged to include you in this shared orthodoxy
(of truth and goodness and beauty and justice, etc.--the "positive values")
then my sense of ecosystemic balance 
is dissonant enough to exclude you
from your rightful place in our radically cooperative eco-space.

I tend to over-react to your negative deviance,
all that nastiness, really?!
because of our culturally collective cognitive dissonance
about your coincidental positive deviance,
OK, so you are loyal to a fault and a good cook,
and the clothes actually do smell and feel better when you do the laundry,
although it is the environmental expense that we actually disagree about,
whether it is significant to our collective future, 
or not,
or something in between,
some place that we might actually find
and consensually agree about
and then go on to those other kinds of sensuality,
but I think I have side-railed here.

Perhaps we enjoy solidarity in rooting for the underdog
in empathizing with those who appear
with a magical potential of a positive deviant outcome.
We so hope the underdog might win this round
in part
because we thereby retain a ray of hope
that we too may someday win
with all our undervalued, unsung, underdogged traits,
cooperative preferences,
nurturing instincts,
suffering and struggling with
my over-dog egocentric cultural landscapes,
my environment,
my internally encultured ego (Left-brained) consciousness.

I always cast my ego in the role of underdog,
just as my Right brain casts our permaculturally cooperative eco-consciousness
in the role of Superdog.

This internally chaotic conspiracy of self-doubt
about ego's capacity to live fully,
integrally,
creatively,
honestly,
compassionately,
with appropriate integrity of self-disclosure,
without the embarrassment of closeted hypocrisy,
dropping our considerable weapons of mutual immunity
and cognitive dissonance,
is also the boundary face of rediscovering our Right-brain's ecocenter,
our Beloved non-verbal Communication center,
comprehensively conscious,
resonant and resolved,
optimized and polypathically densely nutritious,
only through bicamerally synergetic confluence,
active peace,
love,
integrity of shared meaning and purpose
to the very core of our mutually messianic
mutually mentoring
co-redemptive
ego-and-eco balanced chi-soul.

Interior Landscaped Ego (left)
and Cooperative Exterior Landscaped EcoEarth (right-elder)
DNA/RNA fueled and functional frequencies
coincidentally confluate,
stir
decompose
to regenerate.

Queen Gaia
of Earth's Shabbat
is here to speak today.

Unfortunately,
she can only sign,
and the only way she can see
is through our DNA/RNA fractally-balancing syntax,
so she has asked if she could respond to your questions,
as she understands them
within Time,
who are her TransParent Gender Memories,

YangGod, of Physical Convex Special Case Universe,
and Goddess YinYin,
of metaphysical RNA-temporal syntax,
both bilaterally and bicamerally-reiteratively balancing
Earth Tribes of organic ecosystemic processors,
and planters and dialectical planners,
with interdependently balancing consumer and production functions,
exegeting iconic communication
about natural-empirical facts of Earth's nutritional life,
with Zero-centric dialectical neutral tone and energy
and spacetime,
+/(-,-) neural-synaptic/aptic
ecotemporal balance of Time's transparent memory.

Wow, go Gloria,
you optimize my Mother's BiCameral Pretensions
with such dense summary
of WinWin's PolyCultural HealthCare and Safety CQI 
CoOperative Agenda!

About which we are facing some increasingly climatic issues
of ecosystemically pathological trends
throughout our full RNAcentric EcoLens,
and through our DNAcentric AnthroLens,
where correlational trends
of human political and economic and nutritional systemic ends
of all paradigmatic cultural dialects
are now at both high and deep levels of pathological risk,
as well as polycultural and cooperative health opportunity
to mutually embrace this Transitional Time,
remembering our Golden Rule applies
through both our AnthroLens
and our EcoLens.

Thank you for that background summary
of your unfortunately limited synergetic flow power
during this Yin-recessive moment
within YanGod's precessive, evolutionary transition
toward full-balancing Interior with Exterior,
Ego with Eco, DiPolar Identities
of Time's polycultural diversity.

I don't know how many questions you will invest
with all your climatic signing
necessary to be heard and seen right now,
trying to gently calm all the "Loser!" angers and fears
within critical-transitional, revolutionary change,
so I will ask my personal favorite
because I find it so curious:

"Queen Gaia, don't you think it would be Bodhisattva Warrior timely
to come out of your bisexual agenda closet?"

You know, that is one of my favorite questions too,
in part because it took me so long to hear it.

It is difficult to hear and comprehend climatic questions
that you are confident you have already responded toward,
signed with sufficient redundancy
as to be ridiculously ubiquitously flying in obviousness.
Of course our RNA and DNA memory embryonic strings
are full dipolar-engendered,
so how could Queen Gaia of Shabbat's historical-cultural Creation Story
be anything other than TransParent Yang/YinYin as WinWin
evolutionary co-gravitational thermodynamic revolutioning balance
of BiLateral-Reiterative Genetic Time?

Species of systems,
like any possible imaginable metaphysical use of the word "system,"
must have Yang/Yin balanced-governance economics
to interdependently sustain synergetic dynamics,
positively healthy regeneration trends
capable of consumer and/or producer systemic function.
Neutrally (0)-balanced ecosystems,
sustained in RealTime cooperative interdependence,
are Positive-PolyCultural trending
and Negative-MonoCultural trending
dipolar BiNomial Balance of at least outsideness
as appositionally equivalent double-binding insideness,
cogravitational boundary of surfing BiGenderative Time.

So, yes,
Queen Gaia is BiGenderal
and therefore Shabbat signs
with DiPolar Syntax language,
with normative-neutral
ecosystemically BiGendering 
positive/light OVER negative/dual-bound transparent
equi-valent 4-seasons
of dialectical reason and co-intelligent in-formation
eco-flowing optimized,
nutritional flow of healthy resonant resolutional wealth,
celebrating Yang/Yin Golden EcoBalancing Rule
of Love/Synergy 
as co-arising Presence of mutual gratitude
for my Gift-It-Forward
ecologically evolutionary politically inclusive economy.

See, I knew we were sisters!
I mean,
how could the root nature of Time's Positive
equals Negative
climatic energy Shabbat
not continuously and confluently declare your BiGenderal
BiCameral
EcoConscientific Beauty!

Thanks. That means a lot,
especially right now
as we have arrived together
at such a critical moment.

OK, next question?

Well, perhaps I would add,
in defense of our timing
on this transgender balance of nature issue,
you do realize, I hope,
that millions of people
throughout Earth's ages
living within some level of transgender identity,
other than BusinessAsUsual missionary crusading hetero-anthro,
have understood "Queen Gaia of Shabbat"
quite deviantly from a Jewish concept
of a Queen Bee?
There are diverse nuances for "Queen"
which do not easily translate across dialects.

I can't tell you the number of times
we have looked in a lake or a river or a mirror
and imaged Queen Gaia in drag.
Imaging possibilities is how we recreate together,
usually within our own subcultural dialects.

Just as mutually therapeutic responsibility
is how we regenerate
as cooperative individuals
and as a species
and as this entire Shabbat Paradise-Potentiating Planet
of Earth's RNA/DNA ReGenerative Trees,
InFormating EcoMemory Rivers
dipolar rooting FireGod's transparent compost
of LoveLight to WinWin,
articulating (0)-centric 4D
photosynthetically 
endosymbiotically cellular
transformationally
diastatically optimizing natural growth trends
toward just-right Yang/Yin balanced exchange atmosphere
for Queen Gaia of Shabbat
to rise and shine sustained.

You do realize that you can sign what you just said
a lot faster than all the redundant nuances of my language
can capture,
trying to mono-transculturate polycultural regeneration?
I'm having trouble keeping up with you.

Well, try slowing down
looking at trees,
contemplating their root systems,
noticing how under-standing revolves 
eco-normics of a political integritree.


We might do well
to worry less
about including the grizzly bear population
in our DNA/RNA cooperatively encultured Golden Rule,
after all,
we already would kill and eat them,
if hungry enough,
as they would like to treat us.

We could do well
to become happier
about including the trees and bushes and grass populations
in our RNA-Elder sun/moon-centric Golden Rules,
after all,
we are all on this sun v. moon dipolar co-arising evolutionary ride
together,
and it is more fun to ride
with healthy friends and allies
and co-investors,
rather than our victims,
and brown and grey and green aliens,
and those who would be healthier
to be free of us 
since we became over-Yang sapien Win/Lose evolutionary-mythic predators
struggling against our predative future death, 
competing for quality self-care Time,
midst all these lesser co-empathic beings of co-arising light and ergodic and bionic-ionic cause/effect nondual dipolarity,
of mutual subsidiary political-eco-normic balance.

Are our green and brown friends and allies
doomed to die without us?
I think not, this time.
I think their not-death is our regenerative-cooperative
dialectical health-plan intelligence 
of nature-enculturing time's embryonic unfolding
prime relationship of Ta(o), 
as bilateral transparent (0)-soul Time, 
binomially universally-metaphysically eco-balanced,
as Group Theory smooth-structured RNA-4D Revolutioning
ThermoDynamic Principle of EcoBalance,
and Evolutionary Game Theory fractal-structured
DNA-3D/bilaterally nondual co-arising dipolar time-linear-neural-syntax.

Probably in response to DNA's overly dominant Leftbrain
language as domestication of eco-synergetic-empathy, 
ego/eco =Left/RightElder bicameral development issues 
and industrial-strength growth of pace and race 
away from natural-RNA-rooted wisdom of warm/cold, light/dualdark transparency of organic EarthTime's healthy seasons, 
and dipolar-InteriorANDExterior polyculturally nutritious health co-opportunities,
discontinuance of Ego chaos-dissonance
currently replacing RightBrain understory enculturing vocations,
producing healthy and beautiful flowers
trending toward nutritious
embryonic
rich compost as fuel-enculturing time-codexed
messages of mutual subsidiarity roots
growing cooperative healthy branches.
RightBrain vocations
and embryonic cooperative 
bicameral
political-economic primal-health-development ecosystems.

Cooperative trees and forests
produce roots and dipolar-functional branches
of discontinuous interdependent consumers
within productive root-systemic nutritious industry,
stretching back toward sun and moon-light memory
temporal-neural synaptic+Convex,+ConcaveConvex =
(-,-)LoseLose (0)-soul source 
of bilateral Time as PreEmbryonic CoArising Eco/EgoBirth of Balancing
Group EcoTheory DiPolar Dialectic Parameters of Universal Field-Dimensions,
revolutioning con-science of time's natural enculturation,
space and place emerging grace 
of nondual co-arising/gravitating 
polyculturing YangSpaceFold informing-absorbing from YinYinTime-BiLateral UnUnFractalFold,
DNA/RNA MutualCommons-c-square-light/dark rooted.

Natural systems, like trees and grizzly bears,
incarnate Time's enculturation
of Earth
double-binding-emergent ecosystemic home, 
flying through co-arising time's ecological transportation
and communication
and mutual-investment autonomic-empathic system.

Double-binding
as each Present Moment
is both preformed by past
and book-ended by past and future evolutioning symbiotic tensions
as pretensions predicting healthier retentions,
stretching toward positive nutritional flow,
toward regenerative health of future Time.
All nutritional sensory-neural
DNA/RNA-signaged bilateral roads,
lead both to and from 
internal-convex balancing external concave homes,
temporal-neural-nomial midway tipping point flow
as Health Optimizing Continuous Quality Improvement
of InFormation PolyNomial Abundant Yang exterior-facing
reverse-balancing ExDiPolarFormation [N(NP) spacetime]
appositionally dialectic YinYin interior RNA-co-empathic
DNA/RNA eco-confluent WinWin Evolutionary Game HealthStrategy,
assuming (0)-soul
nondual co-arising dipolar
universal-temporal-bilateral reposition/disposition,
Fold-UnFold binomial EarthTribe-centric
Golden Rule Theorem for eternal self-perpetuation,
or at least a whole lot longer than otherwise

When human nature-culture
turns its back on grizzly and tree root-RNA health-synergetic outcomes,
to consider more metaphysically-inclined
smooth-structured
universal diastatically balanced 
bicameral minds with temporal dipolarity,
thermodynamic balance assumptions of DNA/RNA syntax-season ecological confluence, bilateral ego/eco co-empathic agreement,
co-arising regnerative memory system development
for enculturing future of Time's health and safety,
polyculturing prodigious when not polypathologizing prodigal,
RNA's Elder SunGod-EarthMoonGoddess,
ecoworshipping root cooperative information systemic networks
of communication and mutually subsidiary 
WinWin political and economic regenerate-revolution 
as ecological DNA/RNA co-temperate investment
balancing divestment of monocultural waste and loss,
high risk behaviors for postmillennial regenerators 
of healthy-safe EarthTribe Time.

It is our grizzly nature-cultural conditioning
that presents a negative tsunami of a communication problem
between changes of internal/external climates,
and how to revolutionarily reply,
yet with minimum loss to nutritional values for any life,
whether a life/loss exclusive to our Ego-Interior,
or also without,
in our Exterior EarthTribe Landscapes.

According to Thomas Kuhn,
we're more about discontinuous
internally incommensurable, cultural values,
where wild ego-competition is always languaged 
and deductively scienced,
yet domestic-inductive co-empathic nondual cooperation 
remains prelanguaged,
waiting this Great Transition Revolving EcoResonant Resolution
to polyculturally relanguage our healthy and inclusive norms,
conscientific resolve.

When passion plants a multicultural seed,
then justice flourishes a polypathic trusting flower.

Permaculture and polyculture, 
grow holistic cause-effect karmic significance 
for our physical, and mental, political and spiritual health.

Permacultural, as I intend it this morning,
refers to Yang’s power for nutritional sustainability of natural systems; 
health-power 
that is universally comprehensive consciousness
mindful. 
Permacultural wisdom is rooted in ancient Golden Rules and Ratios 
balanced spiritual proportion and right natural relationship 
between ego and eco, between self and partners, 
family, 
tribal environment.

Polycultural gardens and landscapes,
whether natural-exterior or human natured-interior,
are positive outcomes anticipated, 
designed,
beloved by Organic-Harmonic Permaculturalists.

The opposite  of  polycultural paradise
we might describe as:
1. monocultural (not multiculturally therapeutic)
2. monopolistic and dominating (not mutually cooperative governance, economics, as ecologic)
3. monochromatic (not polymorphically-polypathically natured, regened, generated, evolved, not full octave frequencies of color and harmony).

Permacultural development is to Yang’s force and power.
as Polycultural outcomes are to Yin’s therapeutic flex and flow.


And so it is that in this our permacultural parable, 
One winter of discontent, about 1000 years from now, and more, and less, the Universalist Prophets of Justice turned rather coldly upon the Unitarian Mystics of Warm Compassion.

What happened to Truth, Justice, and the American Independent Way of Freedom; low risk, high yield economic and political life? 

So, as was their practice, these suffering ReGenesis Community Yin-Mystics of too-great compassion went off to hibernate this harsh dark justice, to decompose this permacultural puzzle of the thrival of the economic fittest, and yet also fattest. How could it be that competing weapons of bloated wealth are more powerful than our compassionate Gaia Goddess of ecological “why can’t we all just play cooperatively”  wisdom?  How could an omnipotent benign Unitarian Hostess give birth to litters of runtish parasites without giving them at least a flat playing field for winning more positive outcomes than the dinosaurs?

Following gratitude for winter’s metamorphic suffering and chronically stressed tough-love teachers,
Grandmother Moon responded with polycultural wisdom of waxing and waning hope for spring’s new life:

When winter’s suffering composts in each person,
compassion grows more inclusive and diverse, 
richer, more fertile root systems,
arguing with rather than arguing against,
struggling with rather than struggling against.

Composted in the family,
co-passion will optimize wealth of nutritional values for all senses, feelings, awareness;
Composted in the neighborhood and your local cooperative economy, 
and political platforms, policies, plans,
co-passion will positively slow-growth multiply;
Organically composted throughout the nations,
cooperative ownership and lifestyles could optimize economic and sociotherapeutic regenerativity,
recreating cooperative Win-Win cultural assumptions
from that old-school pre-millennial Win-Lose competitive economics,
permaculturaling our wealth of nations.

During the subsequent long warm summer days
of maturing gardens and wisdom, 
the ReGenesis Community’s Universalist Justice Prophets of the Unraveling Future
and Unitarian Compassion Mystics of Reweaving Cultural Herstory,
stewed this steamy stone soup compost.

Each prophet and mystic, Yanger and Yinner, Universalist and Unitarian, 
shares his and her struggles with injustice and need, 
we sing our segregating sexual, racial, ecological, economic, political, historical and cultural hurt and disappointment,
including every “my nature matters” message and slogan and sign of impending flying apart, rather than investing in flying together.
We grapple for life fully lived in the future,
at least as well as now.

True justice is no more anthro-centric than ego-centric. No more ego-centric than Left-brain dominant. 

Perhaps our permacultural justice opera is sung in a difficult and challenging key, but it cannot be a song if there is no full-octave key accessible within each, and equitably shared by all.

Compassion seeds suffer and burst, struggle and strain, first within our dark winters,
toward ego-Left and eco-Right balanced root systems,
seeking peace-filling integrity of justice for ourselves, 
and then others,
our interdependent co-passionate mentors and messiahs,
and then Earth Herself, with all nature’s species and Tribes,
within all revolving time,
advocate for all generations of life.

Universal Justice expands up and out Yang from Unitarian compassion roots,
Yang from Yin, 
mutually consuming and productive cycles of becoming fit to thrive together.

Universal Justice flowers from Unitarian bicultural yang/yin balance,
as Left to Right hemispheric balance,
as West to Eastern cultural wisdom,
as space from time’s unfolding,
rhythm from rhyme’s iconic order,
rational logic from eco-logically informed systemic function,
deductive reason discerned from inductive,
experiential,
reconnecting wisdom.

Left from Right
as regathering nature from regifting Elder spirits,
as belonging grows from longing to reconnect,
as July’s bloom emerges from January’s gloom.

Communication of justice,
to be communication at all,
must be a cooperative enterprise;
not a competitively punishing exercise in dominatrix.

This multicultural kinda “beloved” justice emerges from cooperative co-passionate vocations 
with and for and of all Earth’s Tribes, species, trees and forests and oceans.
Polycultural justice equivalently loves all Earth’s mutually grateful, resonant, seasons and generations,
including summer’s heated gratitude for the suffering sadness of winter,
Polycultural justice invites all Earth’s Past and Future Redeemer Regenerations to Universally Permacultural Life.

In 1968,
a time of great concern for healthy human civil rights
for and of women as well as LeftBrain culturally dominant men,
Gregory Bateson invited a Symposium
not quite a finished Symphony
proposing Moral and Aesthetic Structure of Human [Climate] Adaptation.

He closed his invitation to show up as follows
[with my own updating Earth Climate Rights commentary in brackets]:

We have perhaps what Sir Geoffrey Vickers has called
an 'ecology of ideas.'
[a health v pathology ecology,
climates of and for ideas,
learning and unlearning climates for therapeutic adaptive/maladaptive purposes].

If it be true that certain people are specially gifted
in the [polypathic multicultural] art of acting upon complex [eco]systems
with [empathic trust/mistrust balancing] homeostatic
or ecological
characteristics,
and that these people do not [co]operate
by spelling out the interaction of all relevant [health/pathology] variables,
then these people must use some inner [health of] ecology
of ideas as an [ecosystemic] analogic model.
(By 'ideas' I  mean thoughts, premises, affects,
[feelings, attendance, listening, relational, empathies]
perceptions of self, etc.)

But if this [empathic trust/mistrust] skill is, in some sense,
really an art [of ego/eco-listening] 
then it is possible that the inner 'ecology of ideas' is a close synonym
of what might also be called aesthetic [affective-cognitive] sensibility [and dissonance].

These notions suggest, finally, that there may be another approach
to the problems of a Theory of 
[Therapeutic EarthRights-HumaneRights] Action.

As I write this, on November 5, 1968, the nation is voting to choose a President
and the voters are faced by alternative candidates--
none of whom even claims to have either [ecological] aesthetic
or [ecopolitical] biological insight
into the [empathic healthy trust] affairs of a large [cooperative] nation.

Be that as it may,
I suggest that before we proceed to a consideration of theories of [therapeutic] action, 
we should devote some time to the question of aesthetic [ecosystemically healthy-wealth] determinism [favoring power-with over power-over resolutions] 
for the following reasons:

a. It is conceivable that there is a whole other order of determinative [health/pathology] factors,
to ignore which would be as fatal as to ignore the homeostatic [co-empathic trust/mistrust] aspect of biological [nutritional-digestive] systems.

b. It is possible that the aesthetic [truth-as-beauty, symmetry, affinitive proportion] approach, 
with its special emphasis upon [natural] patterns
and the [emergent] modulation of [ecotherapeutic] patterns,
may be a natural development out of mem-theory
and 0-graphs [fractal, 4D binary bilateral metric information prime empty-climate, vacuum of nutritional information, 'wallpaper' or dialectally folding/unfolding landscape group/game theory reiterative-revolving systemic]

c. It is possible that the [co-empathic] aesthetic is in some [bicameral] way
closely related to
or [and] derivative from the cybernetic [genetic-binary, reiteratively double-bind bilateral balancing tree-root nutritional health structure].

d. It is possible that the aesthetic approach may provide short cuts to the [deductive-only] evaluation
and [Left v RightBrain] criticism of plans for [therapeutic] action.

e. It is possible that [basic] aesthetic [empathic trust] perception may be characteristic of [ecologically healthy bicameral-balancing] human beings,
so that action plans which ignore this characteristic
of [Left-Right equivalent] human perception
are unlikely to be [power-with, cooperatively, struggling with as not against] adopted,
and even unlikely to be [cooperatively] practicable
[because not supported by ecopolitical social-cultural dominant structures
despite evolutionary history
as ethological witness to mindbodies of and for health regeneration].

f. It is possible that aesthetic computation and aesthetic creativity are subject to pathological disturbance [mindbody illness]
Certainly creative and artistic processes are in part determined by epoch
and [Left and/or RightBrain dominance and/or equivalent] cultural milieu [climate].
It is likely therefore
that pathologies of culture will produce [ecopolitical] pathologies
of [ugly, terrifying, vacuous, nihilistic] aesthetic perception
and [reductive, seductive iconic] monsters of [mistrusting and ambiguous] aesthetic creation.

g. But, conversely, if the aesthetically [oppositional bipolar either-or Left v appositionally dipolar both-and Right] monstrous
be symptomatic of cultural [ecopolitical climate] pathology,
then we have to remember that in all such [sacred ecosystemic] cases,
the symptom is the [pathology] system's attempt to cure itself [ourselves].
The creation of the appropriate [evil-reverses-live, terrorist, abusive, neglectful] monstrosities might therefore be a component in corrective [purgative] action.
It is possible that some contemporary [subclimates for nutritional landscape optimization permacultural] artists
are actually doing [multiculturally inclusive healthy] things
which we in our conference hope to plan to do
[both economically and politically re-acclimative volution].

For these and related reasons,
I think that we should take a good look at the [climatic] problems
of [empathic trust/mistrust] aesthetics
before we go on to the [ecological] problems of [therapeutic climate] action.

[With Bateson's late premillennial concerns,
we continue to engage our Left-Right bicameral mindbody balancing
equivalent powers within ecological ethics
and ecosystemic aesthetics
felt and learned and exegeted 
through our ecopolitically cooperative therapeutic choices
of and for multiculturally polypathic democracies
of and for Earth as Humane-Home Sacred Rights
both within as without Ta(o)-Zen Centric 
MultiCultural Climate-Health Landscapes.]

He just appeared to me, like wispily curling 
Chimney smoke, 
One grim and early morning in the very midst of 
Decembers briefest days, on the highest slope,
Toiling through my daily round; where, slowly 
Driving up past the Whitethorn hedgerows to 
Ascend the snowy Heys, I had carefully negotiated 
The wide and slowing bend to regain the summit of 
Grappenhalls ploughed and upper-ground.
Stopping the car I stepped out to take a closer 
Look. There he stood: New born and rather wobbly. 
His long blustery mane thick and silky: Liken the
Mythical Enbarr; a wide eyed expression of staring, 
Uncomprehending malaise written all over his 
Shaggy face...So wondrous was he of this icy world 
So rigidly bound.
Perplexed - perhaps, or amazed, at the utter 
Desolation of this cruel place and the callousness of 
The Fates wounding imposition upon him...when 
Thrust forcefully into yonder shattered bowl - shrunken  
Hopelessly into the clutches of such an altogether frozen 
surround!
Little icicles beginning to form upon his fuzzy beard;
A first taste of his mothers hot milk, that, in his 
Awkward blundering, he must have hastily spilt 
When clumsily fumbling with extended and pouting lips 
Upon the swollen teat. The foul weather, so unfortunately 
Adverse, of hail and sleet, gathering more momentum - 
Didst indeed still prevail...increasingly growing 
Steadily even more worse! 
Stood his mother there - resolutely, as if grave Epona 
Depicted in a hewn chunk of Grecian rock! This
Metallic pan he shivered within: The centre of his 
Twirling Universe designated as this one small 
Spot...And all it should ever contain therein. 
A ripping wind that snarled and savagely bit down like 
A pack of wild hunting dogs, oblivious to his obvious 
Distress, into newly formed bones, 
where, stretched across: Tightly pinched muscle and 
Tautly sinewed flesh - involuntarily flinched! 
Whilst all the while, not withstanding despondent 
Resignation, an aggrieved 
Spirit that silently and inwardly bemoans;
Contained here...In his sparkling kingdom of barbed 
Wire and an irregular scattering of smoothly rounded 
Stones.
A torturous blast that blew so raw I stamped my feet, 
As if a horse myself, and exhaled upon my hands, now 
Clasped and sore, vainly trying to reinforce myself 
Against the unrelenting cold; a fearsome breeze 
Howling in rising crescendos, unopposed,
Through the blasted files of battered trees, whose
Roots clawed in desperation at the thin soils of that 
Barren hill, leaving him naked and painfully exposed
To the ruthless torments of a vicious blizzards 
Crippling chill! 
Casting hopefully about I sought to catch sight of a 
Kindly soul, whom, with an imploring stare or polite 
Shout, I could impose upon to relieve the slight laden 
Over the plight of the brave little Foal. Oh staunchest 
Mare: Thou art Impenetrable like the shield of Achilles!
Grimly determined as if to refute the very elements 
Themselves, and dare the brazen God 
Of Thunder - to break! And heap upon this forged and 
Ferrous land when unleashing his indolent Furies -
The mauve and purple clouds to violently tear asunder!
For, gripped in the maw of such a gnawing ire, 
What could you possibly know, little man, of 
Comforting warmth leaping across a cheery hearth 
When stoked and released from the confines of a 
Parlours glowing fire?
Or Vulcans hellish fires bursting forth from erupting 
Volcanoes - when spewed out blistering magmas run!
Majestic fires pervading Angels disrupted heights:-
They whom bear witness to the obliteration of an 
Exploding Supernovas doomed sun!
Fire or Ice...it be all the same: One scorches within a 
Tightening Vice - One within a wanton flame!
Tarried I a while longer, like a man unsure whether he 
Was to be completely overtaken by some momentous 
Event, 
And wondered out aloud: What hardened heart had 
Deserted this poor creature to this inhospitable 
Environment? 
The self same heart that had decreed that he, the 
Finest of this rare breed, should open his eyes on that 
First morn to find his meagre plate encumbered with 
Miseries so devoid, and served with inadequacies of 
Such spiteful forlorn; with nought to sate the ragged 
Edge of his desperate appetites...save his mothers 
Fluids; although, in urgent anticipation, should 
Give him good cause to keenly salivate wouldst barely 
Suffice the discontented juices, that unceasingly 
Complained aloud, to happily digest and
Gratefully dissipate within his hollow bowel.
It was then I suddenly noticed, slowly revealed to my 
Aging sight - Barely thus adjusted and focused to that 
Opaque light, what looked like a black tarpaulin thrown 
Across a bundled pile of straw, still obscured but now 
partially unconcealed, 
Dumped carelessly in a far corner recessed on the 
Furthest edges of this dismal field. 
Could this be his drafty stall? Delivered here, unseen 
And unheard, upon a bed of dried and bleached stalks -
Enabled Like a baby Messiah amongst the Israelites! 
Wherein, comes the crunching night, which coils 
Around his cradled form with damp and insidious 
Vapours, he reclines against the unyielding Dam -
And valiantly Fights... To attain uncontested slumber 
Beneath the refrain of Heavens dispassionate 
Firmaments; whose Great Creator counts and records 
His given number;
The blazing lanterns, admidst rolling oceans 
Of abandonment and disdain, now abruptly parted -
Like the sea of Galilee! Towering waves rolled back 
From the denuded and ageless bar:
Pushed out wide - And far aside...
To usher in the immutable brilliance 
Of one small horses lone and guiding star...

And if I recall rightly, my little friend, I christened you 
There and then...And thereby named you - IRONBAR!

What's up?
Thanks for this second interview,
old man.

You are either blind or confused,
but probably both.

Well, thanks,
and I appreciate you as well.
Now, I understand you want to talk about human consciousness.

We comprehend your language as limiting human consciousness.

Now would that be the royal "we"
or are you assuming something about me
or the entire human race?

Yes, although be careful not to confuse royalty with governance.
Royalty is best democratized for universal
and global
and individual self-governance.
This is the subject of considerable ancient poetry
and wisdom.

OK, well,
how about a wide open question
and then you can just say whatever it is you
or we
want to say about human consciousness?

Was that your wide open question
or am I still waiting for it?

Apparently you are still waiting
because you are continuing to respond to my questions
with questions.

Yes, that's what I wanted to say about human consciousness.
So, any other questions for me today?

I don't know how I got myself involved with you again.
You  are the most ornery pedantic old fart I have ever met.

I resemble that remark
but it is not what I understand as an "open question."

What would you like to say about consciousness?

Thank you.
That reminds me of the grand opening of Book 1:
The Character of Tao,
entitled "On The Absolute Tao."
Let me try a post-millennial transposition
of Laotse's famous treatise:

Book 1: The CoArising DiPolar Character of Time
1. On Absolute Time

The Time that can be spoken
Is not comprehensive time;
The Languages that can be given
Are not fully PolyPathic-Real
resonate
resolved Information,
or understanding.

Not-Not Binomiality is the origin of "Universe" and "Earth";
Language-Logos-Left hemisphere
proposes to the Right-hemispheric Eco-Mother 
of Earth's Universal Solar-Fueled Nutrition System.
Left speaks ego's anthrocentric voice
to Right's mute eco-centric dipolar balanced syntax.

Therefore:
Oftentimes, humans purge themselves of ego's fear-of-death passion
In order to comprehend Life's Original Intent;
Oftentimes, Universal Time's comprehensive ecoconsciousness regards human co-passion,
To rediscover its bilaterally eternal flowing form
from past into this present toward future's past.

This binomial--yin's secret future time 
with yang's manifest past time--
is one naturally equivalent bilaterally co-arising cycle of consciousness;
Yin-Future and Yang-Past are given different names
When human language explains their bilateral manifestation
in the present
as polypathically binomial
"not not yet"
and
"not not now".

Future "not not yet" with Past Polynomial-Yang empowered Information 
we language through Present's comprehensive consciousness,
Logos-Mythos ReConnection
ReCreation
PermaCultural ReGeneration:
Stretching across Future's Omega Point
down and into Deeper Ecology
Is the Risk and Opportunity Paradox 
of Ego's optimizing LoveLife within Earth's Balancing ReBirthing Death.

Wow, that sounds really deep Dr. Time
but some of us are really busy trying to get through our day
so if you're done
I'll submit this
but don't expect too much by way of positive outcome
cause that was really out there in the effectiveness department.

You sound disappointed.

Let's just agree that comprehensive consciousness
seems to lack sufficient informational articulation
to change how I feel about you,
for example.

I suppose that's why we call it "comprehensive."
So, let's try redirecting fear about future deaths
and anger about past deaths
by including both ourselves and our environment
discovering what anger at,
fear about,
oneself can teach
our present consciousness.

What does your present conscience show you
about your justified anger at others,
past events,
society,
significant others;
what does fear about others,
and your future,
teach you about love and kindness
needed for yourself AND
these others,
together,
as a co-arising correlated relationship through time?

When future-fear and past-anger say
"I don't have time for you."
future-love and past-kindness coincidentally say
"I regret not having enough time for us."

When past-anger says
"I don't have enough time for me."
future-love and past-kindness also say
"I regret not having enough time for me
to be with eco-us, 
universal-us,
governance-us,
to invest in more comprehensive consciousness,
universal intelligence,
to "sit with the world,"
to re-create,
to co-create,
to co-incidate,
to Right-eco-recenter my Left-ego-identity."

When love and kindness say
"I have time for you"
future-fear and past-anger are also saying,
"I regret not having enough time for egocentrism."
but,
future-love and past-kindness only speak within languaged consciousness
when present-tensing time is consciously dominant,
just as future-fear and past-anger only speak
with future and past tense timing dominance.

Anger about past relationships
transactional events within time,
is also fear about replication within future's coincidental space
of present-tense comprehensive consciousness.

I'm feeling dizzy and light-headed.

You are dizzy and light-headed.

I just said that.

Binomially eternal time recycles
reiterates
religioning revolutionary
and enlightening intuitive dipolar headed,
as ego turns to fly home to Right-brain centric embrace
bilateral time regains this human race's natural healthy pace.

Too many words.

That's OK.
His royal commissioner accused Mozart of too many notes.
Both history and culture had their timely response.
Mozart still sings and dances
because he did not listen to repressive governance messages.

Too many notes, I'll never get this submitted in time.

Well, time doesn't wait,
but it doesn't leave any faster than it arrives.
'''

text = text.replace(',',' ')
text = text.replace('.','')
text = text.replace('/','')
text = text.replace('!','')
text = text.replace('?','')
text = text.replace(';','')
text = text.replace(':','')
text = text.replace('~','')
text = text.replace('-','')
text = text.lower()

#adj word count
afrequentwords = []
anum_frequentwords = []
afinal_wordfreq = [afrequentwords, anum_frequentwords]
for repeatedword in awordlist:
    counter = 0
    for word in text.split():
        if repeatedword.lower() == word:
            counter = counter + 1
    if counter>=1:
        afrequentwords.append(repeatedword)
        anum_frequentwords.append(counter)

#noun word count
nfrequentwords = []
nnum_frequentwords = []
nfinal_wordfreq = [nfrequentwords, nnum_frequentwords]
for repeatedword in nwordlist:
    counter = 0
    for word in text.split():
        if repeatedword.lower() == word:
            counter = counter + 1
    if counter>=1:
        nfrequentwords.append(repeatedword)
        nnum_frequentwords.append(counter)

#generating user interface

tk = Tk()
tk.geometry('700x700')
canvas = Canvas(tk, width=1100, height=400, bg = 'white')
canvas.pack()
canvas.pack(expand = YES, fill = BOTH)
def newpoem():
    #generating nouns

    def compositenumgen():
        global x
        x=random.randint(0, len(nnum_frequentwords)-1)
        global compositenum
        compositenum = random.randint(0,7) + nnum_frequentwords[x]
        return compositenum    
    compositenumgen()

    def getnoun1():
        global noun1
        if compositenum > 2:
            global noun1
            noun1 = nfrequentwords[x]
        else:
            compositenumgen()
            getnoun1()
        return noun1
    getnoun1()


    #generating noun 2

    def compositenumgen2():
        global y
        y=random.randint(0, len(nnum_frequentwords)-1)
        global compositenum
        compositenum = random.randint(0,7) + nnum_frequentwords[y]
        return compositenum    
    compositenumgen2()       
    def getnoun2():
        global noun2
        if compositenum > 2:
            global noun2
            noun2 = nfrequentwords[y]
            return noun2
        else:
            compositenumgen2()
            getnoun2()
        if compositenum > 2 and noun2 == noun1:
            getnoun2()
    getnoun2()
            

    #generating adjective 1

    def compositenumgen3():
        global a
        a=random.randint(0, len(anum_frequentwords)-1)
        global compositenum
        compositenum = random.randint(0,7) + anum_frequentwords[a]
        return compositenum    
    compositenumgen3()       
    def getadj1():
        global adj1
        if compositenum > 2:
            global adj1
            adj1 = afrequentwords[a]
        else:
            compositenumgen3()
            getadj1()
    getadj1()

    #generating adjective 2
    def compositenumgen4():
        global s
        s=random.randint(0, len(anum_frequentwords)-1)
        global compositenum
        compositenum = random.randint(0,7) + anum_frequentwords[s]
        return compositenum    
    compositenumgen4()       
    def getadj2():
        global adj2
        if compositenum > 2:
            global adj2
            adj2 = afrequentwords[s]       
        else:
            compositenumgen4()
            getadj2()
        if compositenum > 2  and adj2 == adj1:
            compositenumgen4()
            getadj2() 
    getadj2()

    #generating adjective 3
    def compositenumgen5():
        global d
        d=random.randint(0, len(anum_frequentwords)-1)
        global compositenum
        compositenum = random.randint(0,7) + anum_frequentwords[d]
        return compositenum    
    compositenumgen5()       
    def getadj3():
        global adj3
        if compositenum > 2:
            global adj3
            adj3 = afrequentwords[d]       
        else:
            compositenumgen5()
            getadj3()
        if compositenum > 2  and adj3 == adj2 or adj3 == adj1 :
            compositenumgen5()
            getadj3() 
    getadj3()

    #generating adjective 3
    def compositenumgen6():
        global f
        f=random.randint(0, len(anum_frequentwords)-1)
        global compositenum
        compositenum = random.randint(0,7) + anum_frequentwords[f]
        return compositenum    
    compositenumgen6()       
    def getadj4():
        global adj4
        if compositenum > 8:
            global adj4
            adj4 = afrequentwords[f]       
        else:
            compositenumgen6()
            getadj4()
        if compositenum > 2  and adj4 == adj3 or adj4 == adj2 or adj2 == adj1:
            compositenumgen6()
            getadj4() 
    getadj4()

    global finalpoem
    finalpoem = canvas.create_text(350,200, text= noun1 + " is " + adj1 + " and " + adj2 + '\n' + "Looking at " + noun2 + " is quite " + adj3 + '\n' + "Nature is so " + adj4)

def clearpoem():
    tk.update()
    canvas.delete(finalpoem)

#Good poems and bad poems
    
def goodpoem():
    nnum_frequentwords[x]+=1
    nnum_frequentwords[y]+=1
    anum_frequentwords[a]+=1
    anum_frequentwords[s]+=1
    anum_frequentwords[d]+=1
    anum_frequentwords[f]+=1
def badpoem():
    nnum_frequentwords[x]-=1
    nnum_frequentwords[y]-=1
    anum_frequentwords[a]-=1
    anum_frequentwords[s]-=1
    anum_frequentwords[d]-=1
    anum_frequentwords[f]-=1

#Button
Button(tk, text='Generate new poem',command=newpoem, width=20, height=10).pack(side=RIGHT)
Button(tk, text='Clear poem',command=clearpoem, width=20, height=10).pack(side=LEFT)
Button(tk, text='Good Poem',command=goodpoem, width=20, height=10).pack(side=TOP)
Button(tk, text='Bad Poem',command=badpoem, width=20, height=10).pack(side=BOTTOM)


print (nfrequentwords)
print (nnum_frequentwords)
print (afrequentwords)
print (anum_frequentwords)


