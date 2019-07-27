HOUR_RUN_STOCK=16
MINUTE_RUN_STOCK=15

while [ 1 ]
do
    HOUR=`date +"%H"`
    MINUTE=`date +"%M"`
    DAY_OF_WEEK=`date +"%u"`
    if [ "$DAY_OF_WEEK" == "1" ] || [ "$DAY_OF_WEEK" == "2" ] || [ "$DAY_OF_WEEK" == "3" ] || [ "$DAY_OF_WEEK" == "4" ] || [ "$DAY_OF_WEEK" == "5" ] ; then
        echo "Run TaiwanStockMonitor at 星期${DAY_OF_WEEK}, ${HOUR}點${MINUTE}分"
        if [ "$HOUR" == "$HOUR_RUN_STOCK" ] && [ "$MINUTE" == "$MINUTE_RUN_STOCK" ]; then
        python Stock_TWSE.py
        python Stock_TWT38U.py
        python Stock_TWT43U.py
        python Stock_TWT44U.py
        stock_id="2498"
        python Parser.py ${stock_id}  >> ${stock_id}.txt
        stock_id="2454"
        python Parser.py ${stock_id}  >> ${stock_id}.txt
        cd TWT38U
        git commit -am "Update 外資買賣資訊"
        cd ..
        cd TWT43U
        git commit -am "Update 自營商買賣資訊"
        cd ..
        cd TWT44U
        git commit -am "Update 投信買賣資訊"
        cd ..
        cd data
        git commit -am "Update 上市櫃買賣資訊"
        cd ..
        git push
        fi
    else
        echo "Today is Saturday or Sunday. You should go to outside and do some exercise."
    fi
    sleep 60
done
