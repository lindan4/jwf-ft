$(document).ready(function () {
  $("#calculate-cost-btn").click(function () {
    // Get distance
    let distanceVal = $('input[name="distance"]').val();
    if (distanceVal == "other") {
      distanceVal = $("#distance-other-input").val();
    }
    // Get weight
    let weightVal = $("weight-input").val();
  });
});
