foamToVTK -fields '(p U)' > post.log 2>&1
python3 plotVelProbe.py >> post.log 2>&1
