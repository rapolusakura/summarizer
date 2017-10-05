{% extends 'base.html' %}

{% block content %}

<div id="main">
    <form action="{% url 'main' %}" method="POST">
        {% csrf_token %}
        <br/><textarea style='padding:5px' type='text' name='subject' id="txt" class="one" class="grid" rows=3 cols=30 autocomplete="off" placeholder="What would you like to summarize?"></textarea>
        <br/><input style='padding:5px;margin: 20px' type='text' name='number' placeholder="How many sentences?"/>
        <br/><input style="margin: 5px" type="submit" value="Summarize Text"/>
    </form>
</div>
{% endblock %}
