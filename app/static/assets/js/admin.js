$(document).ready(function () {
  $("#status-message").hide();

  $("#submit-new-coefficients-btn").click(function () {
    // Get existing coefficient p elements
    let existingDistanceCoefficient = $("#distance-coefficient-val");
    let existingWeightCoefficient = $("#weight-coefficient-val");

    // Get distance coefficient
    let newDistanceCoefficient = $("#new-distance-coefficient");

    // Get weight coefficient
    let newWeightCoefficient = $("#new-weight-coefficient");

    // Validate input fields
    if (
      newDistanceCoefficient.val() == "" &&
      newWeightCoefficient.val() == ""
    ) {
      // Display error message
      $("#status-message")
        .text("One or more coefficients are required.")
        .show();

      return;
    }

    let inputDistanceCoefficientVal =
      newDistanceCoefficient.val() != ""
        ? newDistanceCoefficient.val()
        : existingDistanceCoefficient.text();
    let inputWeightCoefficientVal =
      newWeightCoefficient.val() != ""
        ? newWeightCoefficient.val()
        : existingWeightCoefficient.text();

    inputDistanceCoefficientVal = Number(inputDistanceCoefficientVal).toFixed(
      2
    );
    inputWeightCoefficientVal = Number(inputWeightCoefficientVal).toFixed(2);

    $.post(
      "/admin/update_coefficients",
      {
        new_distance_coefficient: inputDistanceCoefficientVal,
        new_weight_coefficient: inputWeightCoefficientVal,
      },
      function () {
        $("#distance-coefficient-val").text(inputDistanceCoefficientVal);
        $("#weight-coefficient-val").text(inputWeightCoefficientVal);

        $("#status-message").text(
          "Coefficients have been successfully updated"
        );
        $("#status-message").show();
      }
    );
  });
});
