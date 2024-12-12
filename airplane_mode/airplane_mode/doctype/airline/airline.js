// Copyright (c) 2024, Akshata and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
    refresh(frm) {
        let link = "https://www.goindigo.in/";
        frm.set_value("website",link)
        if(frm.doc.website){
        frm.add_web_link({
            "label":"Visit Website",
            "url":"https://www.goindigo.in/"
        })
    }
    },
});
