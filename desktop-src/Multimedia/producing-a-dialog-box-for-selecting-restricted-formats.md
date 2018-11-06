---
title: Producing a Dialog Box for Selecting Restricted Formats
description: Producing a Dialog Box for Selecting Restricted Formats
ms.assetid: 486ba928-e06d-4ab0-a642-ba0fe16c8291
keywords:
- audio compression manager (ACM),producing dialog boxes
- ACM (audio compression manager),producing dialog boxes
- ACM examples,producing dialog boxes
- producing dialog boxes
- acmFormatChoose function
- audio compression manager (ACM),selecting restricted formats
- ACM (audio compression manager),selecting restricted formats
- ACM examples,selecting restricted formats
- selecting restricted formats
ms.topic: article
ms.date: 05/31/2018
---

# Producing a Dialog Box for Selecting Restricted Formats

You might want to use the dialog box created by the [**acmFormatChoose**](/windows/desktop/api/Msacm/nf-msacm-acmformatchoose) function, but limit or control the formats in the dialog box. You can do this by using the ACMFORMATCHOOSE\_STYLEF\_ENABLEHOOK flag to hook the dialog procedure. The application can then filter the formats by responding to the [**MM\_ACM\_FORMATCHOOSE**](mm-acm-formatchoose.md) message in the message procedure for the dialog box.

 

 




