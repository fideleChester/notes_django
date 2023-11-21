### Projet d'application notes






{% extends 'base.html' %} {% block content %}

{% block title %}
    Ajout des notes
{% endblock title %}
    

{% block style %}
<style type="text/css">
    input[type=number], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}


form{
margin-left:10rem;
margin-right:10rem;
border-radius:5px;
padding:2rem;
box-shadow:2px 2px 3px 2px;
}
</style>

    
{% endblock style %}

    
  <form action="" method="post">
    {% csrf_token %}
    <label for="note">La note</label>
    <input type="number" id="note" name="note" >
    
  
    <input type="submit" value="Soumettre">
  </form>

  {% endblock content %}