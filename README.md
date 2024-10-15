# LinkStrip

Python code that strips link extra character data from YouTube that goes to GitHub


### example link

Often on YouTube for **FreeCodeCamp** videos  have a url to the GitHub but have redirect data attached, this code strips that away and returns simply the GitHub repo link.

Project 1 GitHub [https://github.com/TatevKaren/CaseStudies...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGt1bVRmZ2VYay1jV0xvU1pJWWh4d1d5Tk11QXxBQ3Jtc0trSUhUbW9FZXRTSEVhR241SEFRaTVwRjdwRnpFeVQ1eE82VDFGc3VBYnhYNFhEV0RrWm1QM0RzUjZwRGF2MUd2N094c1FYV2h5cFI2V1AyWkhWT1otLUszcktiOWRjZXFyVnpNVzM0aDQ5bEUtM04wTQ&q=https%3A%2F%2Fgithub.com%2FTatevKaren%2FCaseStudies%2Ftree%2Fmain%2FAB%2520Testing&v=FTpmwX94_Yo)

## code

copy the full url 
```
https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGt1bVRmZ2VYay1jV0xvU1pJWWh4d1d5Tk11QXxBQ3Jtc0trSUhUbW9FZXRTSEVhR241SEFRaTVwRjdwRnpFeVQ1eE82VDFGc3VBYnhYNFhEV0RrWm1QM0RzUjZwRGF2MUd2N094c1FYV2h5cFI2V1AyWkhWT1otLUszcktiOWRjZXFyVnpNVzM0aDQ5bEUtM04wTQ&q=https%3A%2F%2Fgithub.com%2FTatevKaren%2FCaseStudies%2Ftree%2Fmain%2FAB%2520Testing&v=FTpmwX94_Yo
```
paste it in the terminal and get a clean link

```
https://github.com/TatevKaren/CaseStudies
```
