---
description: A FirstRun dialog box sequence collects user name, company name, and product ID information. The installer verifies the product ID during this dialog.
ms.assetid: bb77296f-705a-4409-b2ca-a76bbaf7ea57
title: FirstRun Dialog
ms.topic: article
ms.date: 05/31/2018
---

# FirstRun Dialog

A FirstRun dialog box sequence collects user name, company name, and product ID information. The installer verifies the product ID during this dialog.

A FirstRun dialog box sequence is usually not a part of the action sequence and is instead called by the [**MsiCollectUserInfo**](/windows/desktop/api/Msi/nf-msi-msicollectuserinfoa) function on the first run of the product.

An author of an installer package may use the template dialog sequence or create a different sequence. The dialog sequence however needs to have the user set the following properties:

-   [**USERNAME**](username.md) property
-   [**COMPANYNAME**](companyname.md) property
-   [**PIDKEY**](pidkey.md) property

The product ID will be validated during the dialog using the [ValidateProductID action](validateproductid-action.md) or the [ValidateProductID ControlEvent](validateproductid-controlevent.md).

If the product ID is set as a property on the command line, or by a transform, then the necessity of having the user reenter the product ID during the first-run dialog can be circumvented by controlling the display using the [**ProductID**](productid.md) property. Following the successful validation of the product ID the **ProductID** property is set to the full, valid product ID.

 

 



