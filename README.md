Testing conda-environments for:
* cross platform transfer
* reproducibility
* integration within CI-process

## On local machine (using macOS)

- create a fresh conda environment
- install `numpy, scipy, pandas` in this environment
- use `conda env export > env.yml` and add `env.yml` to this repo
- use `conda env export --no-builds > env-no-builds.yml` and add `env-no-builds.yml` to this repo
- create at least one test script that can be used to see if the environment does what it should
- commit+push this to an empty github repo

## For the github repo

- create a [travis CI job](https://travis-ci.org/), that recreates the environment with conda
- inside this environment, run the test code
  + under macOS
  + under linux


## Expectations:
 `env-no-builds.yml` works on any platform and `env.yml` doesn't work on linux (as local machine uses macOS).

