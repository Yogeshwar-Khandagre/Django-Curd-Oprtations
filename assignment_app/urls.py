from django.urls import path, include
from.import views

urlpatterns = [
    path("",views.insertpageview,name="insertpage"),#its helpful for render HTML page in browser
    path("insert/",views.insertData,name="insert"),#name jo htpl page ko ye btayega ki ham uska view chahte hai uske liye ham
    path("showpage/",views.showpageview,name="showpage"),
    path("Editpage/<int:pk>",views.Editpageview,name="Editpage"),
    path("update/<int:pk>",views.updatedata,name="update"),
    path("delete/<int:pk>",views.deletedata,name="delete")                                       
    
]
