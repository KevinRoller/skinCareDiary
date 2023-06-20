# head_out_idx=[n1,n2,n3,n4,n5]
# head_out={}
# for idx_layer, blk in enumerate(self.blocks):
#     x = blk(x)
#     if idx_layer in head_out_idx:
#         head_out["head_"+str(idx_layer)]=x
import datetime
def getCurentDateTime():
    now=datetime.datetime.now()

    return  {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
        "microSecond":now.microsecond
        }

print({"abc":123,**getCurentDateTime()})