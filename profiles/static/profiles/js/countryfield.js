/* jshint esversion: 6 */

let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#b8bac0');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#b8bac0');
    } else {
        $(this).css('color', '#f1f1f1');
    }
});