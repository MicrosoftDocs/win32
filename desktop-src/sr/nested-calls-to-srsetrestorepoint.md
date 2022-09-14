---
title: Nested Calls to SRSetRestorePoint
description: This topic describes support for nested calls to SRSetRestorePoint through the BEGIN\_NESTED\_SYSTEM\_CHANGE and END\_NESTED\_SYSTEM\_CHANGE event types.
ms.assetid: ee2dea47-f95d-4293-ac33-eff622b84db6
ms.topic: article
ms.date: 05/31/2018
---

# Nested Calls to SRSetRestorePoint

This topic describes support for nested calls to [**SRSetRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srsetrestorepointa) through the BEGIN\_NESTED\_SYSTEM\_CHANGE and END\_NESTED\_SYSTEM\_CHANGE event types.

Applications can safely call [**SRSetRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srsetrestorepointa) when using these event types. The first call to the function creates a restore point. Subsequent nested calls to the function do not create restore points. For example, suppose an application makes the following calls to **SRSetRestorePoint**:<dl> For restore point A with dwEventType = BEGIN\_NESTED\_SYSTEM\_CHANGE  
For restore point B with dwEventType = BEGIN\_NESTED\_SYSTEM\_CHANGE  
For restore point B with dwEventType = END\_NESTED\_SYSTEM\_CHANGE  
For restore point A with dwEventType = END\_NESTED\_SYSTEM\_CHANGE  
</dl>

The second call does not create a new restore point because the call is nested.

 

 




