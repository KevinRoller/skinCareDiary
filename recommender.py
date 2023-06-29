import pandas as pd 
class Recommender:
    
    def __init__(self,path) -> None:
        
        self.df_dry: pd.DataFrame = None
        self.df_normal: pd.DataFrame = None
        self.df_oily: pd.DataFrame = None
        self.make_dataset(path)
        pass
    
    # def load_dataset(self, path:str) -> pd.DataFrame:
    #     return pd.read_csv(path)
    
    def make_dataset(self, path) -> None:
        df=pd.read_csv(path)
        self.df_dry = df[df["skin_type"].astype(str).str.contains("Dry")]
        self.df_normal = df[df["skin_type"].astype(str).str.contains("Normal")]
        self.df_oily = df[df["skin_type"].astype(str).str.contains("Oily")]
    def unroll_product(self,names:list,img_links:list,num:int):
        unrolled={}
        for i in range(num):
            unrolled["product_name"+str(i)]=names[i]
            unrolled["product_img"+str(i)]=img_links[i]
        return unrolled
    def recommend_products(self, num_of_acne: int, skin_type: str) -> dict:
        if num_of_acne <= 5:
            if skin_type == "Normal":
                product_names = self.df_normal["name"].iloc[:90].sample(4, random_state=15)
            elif skin_type == "Dry":
                product_names = self.df_dry["name"].iloc[:90].sample(4, random_state=15)
            elif skin_type == "Oily":
                product_names = self.df_oily["name"].iloc[:90].sample(4, random_state=15)
        elif num_of_acne > 5 and num_of_acne <= 10:
            if skin_type == "Normal":
                product_names = self.df_normal["name"].iloc[90:200].sample(4, random_state=15)
            elif skin_type == "Dry":
                product_names = self.df_dry["name"].iloc[90:200].sample(4, random_state=15)
            elif skin_type == "Oily":
                product_names = self.df_oily["name"].iloc[90:200].sample(4, random_state=15)
        else:
            if skin_type == "Normal":
                product_names = self.df_normal["name"].iloc[200:].sample(4, random_state=15)
            elif skin_type == "Dry":
                product_names = self.df_dry["name"].iloc[200:].sample(4, random_state=15)
            elif skin_type == "Oily":
                product_names = self.df_oily["name"].iloc[200:].sample(4, random_state=15)
        
        if skin_type == "Normal":
            return self.unroll_product(
                product_names.to_list(),
                self.df_normal[self.df_normal["name"].isin(product_names.to_list())]["img_source"].to_list(),
                3
            )
        elif skin_type == "Dry":
            return self.unroll_product(
                product_names.to_list(),
                self.df_dry[self.df_dry["name"].isin(product_names.to_list())]["img_source"].to_list(),
                3
            )
        else:
            return self.unroll_product(
                product_names.to_list(),
                self.df_oily[self.df_oily["name"].isin(product_names.to_list())]["img_source"].to_list(),
                3
            )
