#!/bin/bash

pwd
git_origin=$1
cd git_example
git push ${git_origin} master:master
git push ${git_origin} master:dev
git push ${git_origin} 0.0.0
cd ../

