document.addEventListener("DOMContentLoaded", function () {
    const formsetContainer = document.getElementById("formset-container");
    const addButton = document.getElementById("add-form");
    const emptyFormTemplate = document.getElementById("empty-form-template");
    
    const totalFormsInput = document.querySelector("#id_items-TOTAL_FORMS");
    const initialFormsInput = document.querySelector("#id_items-INITIAL_FORMS");
    const minFormsInput = document.querySelector("#id_items-MIN_NUM_FORMS");
    const maxFormsInput = document.querySelector("#id_items-MAX_NUM_FORMS");

    console.log("Formset initialized with:", {
        totalForms: totalFormsInput ? totalFormsInput.value : "NOT FOUND",
        initialForms: initialFormsInput ? initialFormsInput.value : "NOT FOUND",
        minForms: minFormsInput ? minFormsInput.value : "NOT FOUND",
        maxForms: maxFormsInput ? maxFormsInput.value : "NOT FOUND"
    });

    function updateFormIndices() {
        const allForms = formsetContainer.querySelectorAll(".formset-item");
        
        allForms.forEach((form, index) => {
            form.setAttribute("data-form-index", index);
            
            form.querySelectorAll("input, select, textarea, label").forEach(element => {
                ["name", "id", "for"].forEach(attr => {
                    if (element.hasAttribute(attr)) {
                        const value = element.getAttribute(attr);
                        if (value && value.includes("items-")) {
                            // Replace any existing index or __prefix__ with the new index
                            const newValue = value.replace(/items-(?:\d+|__prefix__)/g, `items-${index}`);
                            element.setAttribute(attr, newValue);
                        }
                    }
                });
            });
        });
        
        if (totalFormsInput) {
            totalFormsInput.value = allForms.length;
            console.log("Updated TOTAL_FORMS to:", allForms.length);
        }
    }

    addButton.addEventListener("click", function () {
        const currentFormCount = formsetContainer.querySelectorAll(".formset-item").length;
        const maxForms = maxFormsInput ? parseInt(maxFormsInput.value) : 1000;
        
        if (currentFormCount >= maxForms) {
            alert("Número máximo de itens atingido.");
            return;
        }

        const newForm = emptyFormTemplate.querySelector(".formset-item").cloneNode(true);
        
        newForm.querySelectorAll("input, select, textarea").forEach(element => {
            if (element.type === "checkbox" || element.type === "radio") {
                element.checked = false;
            } else if (element.type !== "hidden") {
                element.value = "";
            }
        });

        formsetContainer.appendChild(newForm);
        
        updateFormIndices();
        
        const removeButton = newForm.querySelector(".remove-form");
        if (removeButton) {
            addRemoveEvent(removeButton);
        }
    });

    function addRemoveEvent(button) {
        button.addEventListener("click", function () {
            const formItem = button.closest(".formset-item");
            const deleteInput = formItem.querySelector("input[name*='-DELETE']");
            
            const visibleForms = formsetContainer.querySelectorAll(".formset-item:not([style*='display: none'])");
            const minForms = minFormsInput ? parseInt(minFormsInput.value) : 1;
            
            if (visibleForms.length <= minForms) {
                alert("Pelo menos um item deve ser mantido no pedido.");
                return;
            }
            
            if (deleteInput) {
                deleteInput.checked = true;
                formItem.style.display = "none";
                console.log("Marked form for deletion, form still counts toward TOTAL_FORMS");
            } else {
                formItem.remove();
                console.log("Removed new form completely");
            }
            
            updateFormIndices();
        });
    }

    document.querySelectorAll(".remove-form").forEach(btn => addRemoveEvent(btn));
    

    updateFormIndices();


    document.getElementById("order-form").addEventListener("submit", function(e) {
        console.log("=== FORM SUBMISSION DEBUG ===");
        console.log("TOTAL_FORMS:", totalFormsInput ? totalFormsInput.value : "MISSING");
        console.log("INITIAL_FORMS:", initialFormsInput ? initialFormsInput.value : "MISSING");
        
        if (!totalFormsInput || !initialFormsInput) {
            console.error("CRITICAL: Management form fields are missing!");
            e.preventDefault();
            alert("Erro: Campos de gerenciamento do formulário estão ausentes. Recarregue a página.");
            return false;
        }
        
        const formData = new FormData(this);
        console.log("All form data:");
        for (let pair of formData.entries()) {
            console.log(pair[0] + ': ' + pair[1]);
        }
    });
});