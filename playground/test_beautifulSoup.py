from bs4 import BeautifulSoup

html = """
<html lang="en">
<head>
<title>Current Opportunities</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

</head>
<body>
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                                                                               (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o), \
                                                                                                                                          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-106189516-2', 'auto');
ga('send', 'pageview');

</script>
<script>
$(document).ready(function () {
$('.accordion-toggle').on('click', function(event){
    var target = $(this).data('target');
var match_id = $(this).data('matchid');
$.ajax({
    url: "match-detail.php",
    type: "get",
    data:{match_id:match_id},
    success: function(result){
$(target).html(result);
}
});
});
});
</script>

<div class="container">
<br>
<h4>
<strong>This dashboard</strong> follows the strategy explained in the paper
<a href="https://arxiv.org/abs/1710.02824"> Beating the bookies with their own numbers - and how the online sports betting market is rigged</a>.
<br> <br>
This strategy <strong>does not</strong> predict the outcome of football games. If this sentence sounds strange to you,
please read carefully our paper
and the blogposts <a href="https://www.lisandrokaunitz.com/index.php/en/beat-the-bookies-strategy-explained/"> Strategy explained </a>
and <a href="http://www.lisandrokaunitz.com/index.php/what-does-it-take-to-beat-the-bookies-and-is-it-worth-it/"> What does it take to "Beat the bookies" and... is it worth it?</a>.
<br><br>
Finally, you can also have a look at <a href="https://github.com/Lisandro79/BeatTheBookie">this repository</a>,
which has the code that was used to test and implement the strategy and where you can download the data.
An alternative source for the data is <a href="https://www.kaggle.com/austro/beat-the-bookie-worldwide-football-dataset"> right here in kaggle</a>. Enjoy!
</h4>
<br>
<br>


<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Sport</th>
<th>Match Title</th>
<th>League</th>
<th>Result to Bet</th>
<th>Date</th>
<th>Time to Match</th>
<th>Best Bookie</th>
<th>Best Odds</th>
<th>Mean / Median</th>
</tr>
</thead>
<tbody>
<tr data-toggle="collapse" data-target="#row-2XtRhbHn" data-matchid="2XtRhbHn" class="accordion-toggle">
<td>soccer</td>
<td>Sroda  vs. Unia Janikowo </td>
<td>Poland: III Liga - Group II</td>
<td>1</td>
<td>2021-08-27 17:00:00</td>
<td>01:18:23</td>
<td>888sport</td>
<td>1.67</td>
<td>1.56 / 1.53</td>
</tr>
<tr>
<td colspan="12" class="hiddenRow">
<div class="accordian-body collapse" id="row-2XtRhbHn">
</div>
</td>
</tr>
<tr data-toggle="collapse" data-target="#row-Y9GaC8Qs" data-matchid="Y9GaC8Qs" class="accordion-toggle">
<td>soccer</td>
<td>TSC Backa Topola  vs. Mladost </td>
<td>Serbia: Super Liga</td>
<td>1</td>
<td>2021-08-27 18:00:00</td>
<td>02:18:23</td>
<td>Unibet</td>
<td>1.52</td>
<td>1.40 / 1.40</td>
</tr>
<tr>
<td colspan="12" class="hiddenRow">
<div class="accordian-body collapse" id="row-Y9GaC8Qs">
</div>
</td>
</tr>
<tr data-toggle="collapse" data-target="#row-WEB85mpK" data-matchid="WEB85mpK" class="accordion-toggle">
<td>soccer</td>
<td>Al Taee  vs. Al Feiha </td>
<td>Saudi Arabia: Saudi Professional League</td>
<td>2</td>
<td>2021-08-27 18:15:00</td>
<td>02:33:23</td>
<td>Unibet</td>
<td>2.30</td>
<td>2.08 / 2.05</td>
</tr>
<tr>
<td colspan="12" class="hiddenRow">
<div class="accordian-body collapse" id="row-WEB85mpK">
</div>
</td>
</tr>
<tr data-toggle="collapse" data-target="#row-KxHx72C7" data-matchid="KxHx72C7" class="accordion-toggle">
<td>soccer</td>
<td>Hoffenheim W  vs. Freiburg W </td>
<td>Germany: Bundesliga Women</td>
<td>1</td>
<td>2021-08-27 19:15:00</td>
<td>03:33:23</td>
<td>bwin</td>
<td>1.40</td>
<td>1.31 / 1.3</td>
</tr>
<tr>
<td colspan="12" class="hiddenRow">
<div class="accordian-body collapse" id="row-KxHx72C7">
</div>
</td>
</tr>
<tr data-toggle="collapse" data-target="#row-OY55b3KO" data-matchid="OY55b3KO" class="accordion-toggle">
<td>soccer</td>
<td>Avai U23  vs. Bragantino U23 </td>
<td>Brazil: Brasileiro U23</td>
<td>1</td>
<td>2021-08-26 20:00:00</td>
<td>04:18:23</td>
<td>888sport</td>
<td>3.25</td>
<td>2.85 / 2.795</td>
</tr>
<tr>
<td colspan="12" class="hiddenRow">
<div class="accordian-body collapse" id="row-OY55b3KO">
</div>
</td>
</tr>
</tbody>
</table>
</div>

<div class="container">



</div>

</body>
</html>"""


soup = BeautifulSoup(html, 'html.parser')
for row in soup.select('tbody tr'):
    match_id = [x.text for x in row.find_all('tr')]
    row_text = [x.text for x in row.find_all('td')]
    print(match_id)
