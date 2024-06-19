$(document).ready(function () {
  $("p[id='delivery-cost-p']").hide();

  $("#distance-other-input").on("click", function () {
    $("input[name='distance']").prop("checked", true);
  });

  $("#weight-other-input").on("click", function () {
    $("input[name='weight']").prop("checked", true);
  });

  $("#calculate-cost-btn").click(function () {
    let dcTxt = $("p[id='delivery-cost-p']");

    // Get distance
    let distanceVal = $("input[name='distance']:checked").val();
    if (distanceVal == "other") {
      distanceVal = $("#distance-other-input").val();
    }
    // Get weight
    let weightVal = $("input[name='weight']:checked").val();
    if (weightVal == "other") {
      weightVal = $("#weight-other-input").val();
    }

    if (!distanceVal || !weightVal || distanceVal == "" || weightVal == "") {
      dcTxt.text(
        "One or more fields are missing or are in the incorrect format."
      );
      dcTxt.show();
      return;
    }

    if (distanceVal <= 0 || weightVal <= 0) {
      dcTxt.text("Distance and/or weight must be greater than 0.");
      dcTxt.show();
      return;
    }

    $.post(
      "/calculate_cost",
      {
        delivery_distance: distanceVal,
        delivery_weight: weightVal,
      },
      function (data) {
        console.log(data);
        dcTxt.text(`The delivery cost will be \$${data.cost}`);
        dcTxt.show();
      }
    );
  });
});
