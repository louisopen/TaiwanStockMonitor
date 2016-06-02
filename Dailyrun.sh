HOUR_RUN_STOCK=16
MINUTE_RUN_STOCK=30


while [ 1 ]
do
    HOUR=`date +"%H"`
    MINUTE=`date +"%M"`
    DAY_OF_WEEK=`date +"%u"`
    if [ "$DAY_OF_WEEK" == "1" ] || [ "$DAY_OF_WEEK" == "2" ] || [ "$DAY_OF_WEEK" == "3" ] || [ "$DAY_OF_WEEK" == "4" ] || [ "$DAY_OF_WEEK" == "5" ] ; then
        if [ "$HOUR" == "$HOUR_RUN_STOCK" ] && [ "$MINUTE" == "$MINUTE_RUN_STOCK" ]; then
        python crawl.py
        python TWT38U.py
        python TWT43U.py
        python TWT44U.py
        python Parser.py
        fi
    fi
    sleep 60
done
