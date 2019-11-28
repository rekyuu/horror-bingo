from flask import Flask, redirect, render_template, url_for
import json
from random import randint, sample, seed, shuffle
import time

app = Flask(__name__)

@app.route("/")
def main():
  return _seed_and_redirect()

@app.route("/<int:bingo_seed>")
def seeded(bingo_seed):
  if bingo_seed <= 9999999 or bingo_seed > 99999999:
    return _seed_and_redirect()
  else:
    cell_data = [
      "Movie is titled \"The (something)\"",
      "Title is a single word",
      "Antagonist is never seen",
      "Monster is revealed in the first act",
      "Unfitting music",
      "Group of people split up",
      "Irony",
      "Coming full circle",
      "Protagonist dies",
      "Protagonist is the antagonist",
      "It was just a dream",
      "Teen speak",
      "Titties",
      "Too much gore",
      "Character is drunk or high",
      "Scare during romance",
      "Hackerman",
      "Subverted expectations",
      "Antagonist takes too long to kill someone",
      "Ripoff of another popular film",
      "Good actor in a bad movie",
      "Bad script",
      "Good prosthetic",
      "Bad CGI",
      "Creepy expositional character",
      "Exposition overload",
      "Narration",
      "Hiding in plain sight",
      "Stupid nonsensical choices",
      "Expositional reading",
      "Parody of well-known brand",
      "Evil corporation",
      "Monologuing",
      "Bad acting",
      "Introduction of death fodder characters",
      "Blatant advertisement",
      "Cliffhanger",
      "Time limit to do something",
      "Forced tension",
      "Forced relationship motivation",
      "Questionable motives",
      "Pop culture reference",
      "Classical music",
      "Shaky camera",
      "Lame jump scare",
      "False scare by friend or family",
      "Weapons don't work",
      "Karma",
      "Entire movie is in a single location",
      "Character hangs up too soon",
      "Mass destruction",
      "Flashbacks",
      "Vehicle trouble",
      "\"You should come see this\"",
      "Evil kid",
      "Shower scene",
      "Awkward dinner",
      "Antagonist isn't actually dead",
      "Techno-babble",
      "Bad or outdated technology",
      "Unnecessary tell about current event",
      "Scare by an animal or insect",
      "Political commentary",
      "Environmental commentary",
      "\"I'm going with you\"",
      "Plot armor",
      "Character has a disability",
      "Common literary reference",
      "Person with headphones misses everything",
      "Too many logos",
      "Title drop",
      "Creepy child drawings",
      "Nerd speak",
      "Electronics on the fritz",
      "Something passes by unseen",
      "Zoom and enhance",
      "No one believes events told by character",
      "Ambiguous answers",
      "No phone connection",
      "Plot convenient coincidence",
      "Family in financial trouble",
      "Relationship problems",
      "Characters stick around instead of leaving",
      "Not scary",
      "Inappropriate comedic timing",
      "Off-color sexuality/gender joke",
      "Character falls asleep at inappropriate time"
    ]

    seed(bingo_seed)
    cells = sample(cell_data, 25)

    return render_template("main.html", bingo_seed = bingo_seed, cells = cells)

@app.errorhandler(404)
def not_found(e):
  return _seed_and_redirect()

def _seed_and_redirect():
  seed(time.time())
  bingo_seed = randint(9999999, 99999999)

  return redirect(f"/{bingo_seed}")

if __name__ == "__main__":
  app.run(
    debug = False
  )