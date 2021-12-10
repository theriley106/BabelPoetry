# Babel Poetry

The title "Babel Poetry" is based on a short story called "The Library of Babel" by Jorge Luis Borges.

In the story, there exists this fictional library in which every possible combination of letters, numbers, and punctuation exists. In theory this library would be unimaginably large, but would contain every poem, song, book, legal decision, or scientific paper that could ever be written.

Of course in practice, given the current state of computing this is only possible to a small degree -- for example, it would take 26^79 combinations of characters, or roughly 10^97 years for a computer to generate the following 15 word Rupi Kaur poem:

```
we are all born
so beautiful

the greatest tragedy
is being convinced we are not
```

So of course generating 1:1 copies of a Rupi Kaur poem isn't really something that's feasible with the technology we have today, nor is it even particularly interesting from a poetry perspective, but what if we wanted to generate *new* poems in the **style** of Rupi Kaur? 



One characteristic that I've noticed throughout our class is that oftentimes the same poem can be interepreted differently by different readers -- this is especially true with Abstract poetry.

Computer generated poetry is an interesting branching point from this idea, and it prompts the question -- if you train a neural net on hundreds of thousands of poems, would the new words generated and inspired by the training data be a poem? 

# How It's Made

## Dataset

So unfortunately, there weren't a ton of options available for large datasets of poems, and I knew I needed 

### Plan A - ProjectGutenberg



I was able to find something called Project Gutenburg, which is a project that works to maintain an archive of public domain books and poetry. Project Gutenberg also has a well documented public API, so it was easy enough to write a script that looped through and downloaded every piece of abstract poetry in the public domain:

![alt text](/static/guten.png)

After gathering the dataset containing all abstract poetry from their archive, I noticed 2 things:

- It's difficult to programatically remove text that's *not* poetry from public domain books
- The number of abstract poems in the public domain are relatively limited, so the dataset was simply not large enough to generate quality poems

### Plan B - PoetryFoundation

This ended up being a bit more complex, and you can see the full code in the

Esentially, I wrote a script that looped through every search result on PoetryFoundation and found all poems that had a tag indicating they were an abstract poem:

![alt text](/static/search.png)

For each of the saved URLs it went to the page containing the plain text poem and put it into the dataset:

<p align="center">
  <img src="/static/text.png" width="400"/>
</p>


It took a really long time to download all of the poems...

<p align="center">
  <img src="/static/download.png" width="250"/>
</p>



This resulted in a dataset containing ~9,400 poems, which is the largest poetry dataset available online. 

I wanted to make it available for others to use for academic/research purposes, so I open-sourced this project and put the dataset on Kaggle so people can create more sophisticated poetry generation models:

![alt text](/static/kaggle.png)


# Results

These are a collection of poems that I thought were particularly interesting.

### Dear Son

```
I am proud of you,
because of your kindness,
but I am also proud of you
because I am no stranger
to leaving your life.
I am proud of you because
please tell me what you’re thinking,
when you’re smiling, when you’re laughing, because they are
not your problems, but theirs—
you must be grateful
to have made me this— 
I have no other choice,
but to walk away.
```

### The Most Famous Poet In History

```
The most famous poet in history
is beating his chest,
howling on his chest
and the ground.
The only thing
that keeps him alive is
the way
he breaks. He breaks
not just because of grief,
but of pain.
Beneath the stone
I am not a stone, a dead body,
a man. Beneath
the broken is a weapon
that can be used to wreck
the world.
```

### Mother's Hands

```
This is how my mother’s hands
 changed
 as I grew up.
 I was raised
 by strangers and
 always played by strangers
 ages 16 and 17.
 My father
 was my older brother’s
 teacher,
 the one who taught me
 to cook alone.
 I remember
 his hands
 turning red as he
 died.
 I remember
 the hands
 getting smaller
 each day.
```

### One thing we don't have is love

```
What’s so hard about the world is that it’s a bit too much
which is a big part of the reason I hate everything about it
which is that we’re so good and so beautiful
 
and do we ever get upset at being painted out from all of it?
Is this why my father says it was wrong to leave me when he was just a child?
That’s not how it should be.

Who’s been there to me?
And come on?
How can you be so good at anything?
Is there no way to love another person?
Is there anything we don’t have?
```

### Sober

```
A summer night,
I stayed up late,
watched the clock in the ceiling
and remembered the girls’ names in the kitchen. 
I felt like I was there.
The two-by-fours swam out of the house 
like a bloodhound I wanted to escape from.
I didn’t believe it then.
Now I understand my rooms that I enter by foot to reek of  alcohol.
When the sun sets I think of what I left behind.
This summer is my summer.
```

### Strawberries

```
Strawberries!
Sweet blossom — 
What is that?
This how I’ve always been told:
Play it safe and clear.
I’m old;
I love that,
I’m old.
We can rest
at ease.
```

### 

```
My clothes have been collected
 and I am thus entered
 into the maze of personalities
 I have been seeking.
 I want to work with you,
 putting all my bones
 together.
 My body has been broken
 and especially my head has been
 eaten.
 I am the child
 of memory.
 I have learned
 to leave my place
 and think
 of others.
 I am the child of your breath.
```

### The City Never Sleeps

```
The somber pit of the city with its thick layers of glass
 and stone, and the empty warehouse
 where the giddy light came to us,
 a view of the city from the city,
 a dozen terraces of trees, a view of the entire city
 from the swanky opulence of the opulent palace,
 and the empty courtyard, where all our traumas were
 already tacked onto the image, the new black satellite
 or satellite dish, and the empty whole of the city,
 the sound of a rat on the sidewalk, a rat on the paint
 and the smell of its chorused aroma, the smell of rat —
 the rats in the street, the rats in the room — the rats
 and the whole city, and the empty courtyard,
 the dull vaulting of the heart, and the empty whole
 of the city: the time we spent together,
 the time we shared the city, the time we sat there
 and watched our possessions, the empty courtyard,
 the sleek and commodious apartment, and the empty city,
 the empty city of the soul, and the empty cube
 and the empty glass and the empty sky,
 the empty sky and the empty city,
 the empty city of the soul
 and the empty cube, and the empty sky,
 the empty city of the soul
 and the empty sky,
```

###

```
I remember you.
 No one

 Could have ever imagined

 Who’d captured a more beautiful nation.

 The last recorded photo

 of you writing a poem

 Across the street

           from the old house I remember

 Your voice.

 My eyes were wide open

 When you wrote

 Your last poem

 I kept forgetting you.
```


## Observations

Spacing is really tough to get right.

