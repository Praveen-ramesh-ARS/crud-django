
from rest_framework.views import APIView # module
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class ProductsView(APIView):
	
	
	def post(self,request):
		# print(request.data)
		items = Product(product_name = request.data["product_name"],product_code = request.data["product_code"],price = request.data["price"],gst = request.data["gst"],qty = request.data["qty"],category_reference_id = request.data["category_reference_id"])

		items.save()
		
		return Response("data has been saved successfully") 
	
	def get(self,request):
		data1 = Product.objects.all()
        
		selected_serializer = Selected_Serializer(data1,many=True).data
		# list=[]
		# for i in data1:

		# 	selection={
		# 			"id":i.id,
		# 			"product_name":i.product_name,
		# 			"product_code":i.product_code,
		# 			"price":i.price,
		# 			"gst":i.gst,
		# 			"qty":i.qty
		# 		}
		# 	list.append(selection)
		return Response(selected_serializer)


class Productget(APIView):

    def get(self,request,id):
        try:
            data = Product.objects.get(id=id)
            selected_id = ApplicationSerializer(data).data
            
        except Exception as e:
              
              print("Data does not available",e)
        
        # list = []
        # selection = {
        #     "id":data.id,
        #     "product_name" : data.product_name,
        #     "product_code" : data.product_code,
        #     "price" : data.price,
        #     "gst" : data.gst
        # }
        # list.append(selection)
        else:              
              return Response(selected_id)
        finally:
              print("thanks,try again")

    def patch(self,request,id):
        data2 = Product.objects.filter(id = id)
        data2.update(product_name = request.data["product_name"],product_code = request.data["product_code"],price = request.data["price"],gst = request.data["gst"],qty = request.data["qty"],category_reference_id = request.data["category_reference_id"])
        return Response("Updated Succussfully")
    
    
    def delete(self,request,id):
        data3 = Product.objects.get(id = id)
        data3.delete()

        return Response("Deleted Succussfully")

class CategoryView(APIView):
      def get(self, request):
            data5 = Category.objects.all()
            all_category = Category_Serializer(data5,many=True).data

            return Response(all_category)
      
      def post(self,request):
            #data4 = Category(category_name=request.data["category_name"])
            #print(data4)
            new_category = Category_Serializer(data=request.data)
            print(new_category)
            if new_category.is_valid():
                  new_category.save()
                  return Response("Data Saved.")
            else:
                  return Response(new_category.errors)
            
        

            
        