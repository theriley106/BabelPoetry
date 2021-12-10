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

![alt text](/static/text.png)

It took a really long time to download all of the poems...

![alt text](/static/download.png)

This resulted in a dataset containing ~9,400 poems, which is the largest poetry dataset available online. 

I wanted to make it available for others to use for academic/research purposes, so I open-sourced this project and put the dataset on Kaggle so people can create more sophisticated poetry generation models:

![alt text](/static/kaggle.png)


# Results