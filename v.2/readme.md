Howdy!

The goal of this version is to get back to a baseline model that will work decently well.

The principle issue I'm having right now is that I can't tell if there's any true predictive quality to these events. It seems that all the predictions are simply just a version of "he yesterday we had somne bad protests so today we should have the same or more" -- in that it seems all protesting activitiy is lagging actual predictions. e.g., the model can't get "ahead" of the trends -- it's always lagging. 

Further, the validation set is not improving as the model trains -- the loss is constant, implying that the model isn't generalizable / the model is overfitting on trainging data.


## Some links I wanted to save
[Download GDELT Event Codebook](http://data.gdeltproject.org/documentation/GDELT-Event_Codebook-V2.0.pdf)
[Read more about GDELT 2.0](https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/)
[Explore GDELT Datasets](https://blog.gdeltproject.org/the-datasets-of-gdelt-as-of-february-2016/)