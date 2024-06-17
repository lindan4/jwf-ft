$(document).ready(function () {
  $("#status-message").hide();

  $("#submit-new-coefficients-btn").click(function () {
    // Get distance coefficient
    let newDistanceCoefficient = $("#new-distance-coefficient");

    // Get weight coefficient
    let newWeightCoefficient = $("#new-weight-coefficient");

    $.post(
      "/admin/update_coefficients",
      {
        new_distance_coefficient: newDistanceCoefficient.val(),
        new_weight_coefficient: newWeightCoefficient.val(),
      },
      function (data) {
        $("#distance-coefficient-val").text(newDistanceCoefficient.val());
        $("#weight-coefficient-val").text(newWeightCoefficient.val());

        newDistanceCoefficient.text("");
        newWeightCoefficient.text("");

        $("#status-message").text(data.message);
        $("#status-message").show();
      }
    );
  });
});
