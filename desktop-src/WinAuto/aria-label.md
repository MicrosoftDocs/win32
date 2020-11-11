---
title: ARIA Label Error
description: ARIA Label Error
ms.assetid: DF45E38D-9AD3-48C8-911E-8C6233F17F43
keywords:
- AriaLabelErrorId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Label Error

## Text

Element is of type **input**, **button**, **image-button** or **landmark** but doesn't have an accessible name.

## Type

Error

## Description

This error applies to:

-   Form input fields:
    -   HTML tags—**input\[type= "text\|password\|checkbox\|radio\|file\|email\|tel\|color\|date\|datetime\|datetime-local\|time\|week\|month\|number\|range\|search\|url"\]**, **select**, **datalist**, and **textarea**.
    -   WAI-ARIA roles—**checkbox**, **combobox**, **listbox**, **radiogroup**, **radio**, **textbox**, **tree**, **slider**, and **spinbutton**.
-   Images/image buttons/ buttons
    -   HTML tags—**img**, **input\[type="image\|button"\]**, and **button**.
    -   WAI-ARIA roles—**img** and **button**.
-   Landmarks
    -   WAI-ARIA roles—**region**, **banner**, **complementary**, **contentinfo**, **form**, **main**, **navigation**, and **search**.

> [!Note]  
> AccChecker shows this error even for elements for which the accessible name is set by default based on inner HTML content (see the **banner** element in the above example). For these cases, you can suppress this errors.

 

All semantically important UI elements such as form fields (for example, **input**, **select**, **textarea**), images, buttons and landmarks (tags representing logical regions) must have the accessible name to allow screen readers to correctly announce them.

To fix this error, set the accessible name in one of the following ways (listed in the order of preference).

-   Form fields: Use the **label** tag and set the **for** attribute to the **id** value of the target field.
-   Image/image button: Set the **alt** attribute.
-   Buttons: Set the button caption text.
-   For any element:
    -   [**aria-labelledby**](https://developer.mozilla.org/docs/Web/Accessibility/ARIA) attribute: Set to the **id** value of the element containing the accessible name string.
    -   [**aria-label**](https://developer.mozilla.org/docs/Web/Accessibility/ARIA) attribute: Set to the accessible name string.
    -   [**title**](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/title) attribute: Set to the accessible name string (also create a **tooltip**).

## Example


```HTML
<!-- For landmark tags, set the accessible name by using the aria-labelledby 
attribute to reference the visible headers. -->
<h1 id="formHeader">Application Form</h1>
<form aria-labelledby="formHeader">

  <!-- For input fields, use the LABEL tag with the for attribute. -->
  <label for="fullName">Full Name</label>
  <input id="fullName" type="text" />

  <!-- If there is no visible text that can be referenced, set the accessible 
  name by using aria-label or title attributes. -->
  <input type="file" aria-label="Your photo"/>

  <!-- For images, use the alt attribute. -->
  <img src="…" alt="Uploaded photo" />

  <!-- For buttons, caption text is also used as the accessible name. -->
  <button onclick="processForm()">Send</button>

  <!-- For image buttons, use the alt attribute to define the accessible name. -->
  <input type="image" src="images/moreinfo.png" alt="Show more info"/>

  <!-- For elements with inner text this error can be suppressed because the 
  accessible name is set by default. -->
  <div role="banner">Accessible name set by default</div>
</form >
```



 

 




