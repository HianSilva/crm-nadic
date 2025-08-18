document.addEventListener("DOMContentLoaded", function () {
    const formsetContainer = document.getElementById("formset-container");
    const addButton = document.getElementById("add-form");

    const totalFormsInput = document.querySelector(
        "#id_items-TOTAL_FORMS"
    );

    addButton.addEventListener("click", function () {
        const currentForms = formsetContainer.querySelectorAll(".formset-item");
        const formCount = currentForms.length;
        const newFormIndex = formCount;

        const emptyForm = currentForms[0].cloneNode(true);

        emptyForm.querySelectorAll("input, select, textarea, label").forEach(el => {
            if (el.name) {
                el.name = el.name.replace(/items-\d+-/, `items-${newFormIndex}-`);
            }
            if (el.id) {
                el.id = el.id.replace(/items-\d+-/, `items-${newFormIndex}-`);
            }
            if (el.tagName === "INPUT" && el.type !== "hidden") {
                el.value = ""; // limpa valores
            }
        });

        formsetContainer.appendChild(emptyForm);

        totalFormsInput.value = parseInt(totalFormsInput.value) + 1;

        addRemoveEvent(emptyForm.querySelector(".remove-form"));
    });


    function addRemoveEvent(button) {
        button.addEventListener("click", function () {
            button.parentElement.remove();
            const currentForms = formsetContainer.querySelectorAll(".formset-item");
            totalFormsInput.value = currentForms.length;
        });
    }

    document.querySelectorAll(".remove-form").forEach(btn => addRemoveEvent(btn));
});
