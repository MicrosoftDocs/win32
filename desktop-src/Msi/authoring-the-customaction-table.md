---
description: Enter records for the five sample custom actions created in the previous section to the CustomAction Table. For more information on how to populate the CustomAction table for this type of custom action see Custom Action Type 1.
ms.assetid: 56828105-bd72-426d-833f-f756c577c77f
title: Authoring the CustomAction Table
ms.topic: article
ms.date: 05/31/2018
---

# Authoring the CustomAction Table

Enter records for the five sample custom actions created in the previous section to the [CustomAction Table](customaction-table.md). For more information on how to populate the CustomAction table for this type of custom action see [Custom Action Type 1](custom-action-type-1.md).

[CustomAction Table](customaction-table.md)



| Action            | Type  | Source      | Target                |
|-------------------|-------|-------------|-----------------------|
| ProcessAccounts   | 1     | Process.dll | ProcessUserAccounts   |
| UninstallAccounts | 1     | Process.dll | UninstallUserAccounts |
| CreateAccount     | 11265 | Create.dll  | CreateUserAccount     |
| RemoveAccount     | 11265 | Remove.dll  | RemoveUserAccount     |
| RollbackAccount   | 9473  | Remove.dll  | RemoveUserAccount     |



 

The C++ source code for the dynamic-link libraries are provided in the Windows Installer SDK. Use Process.cpp to create the file Process.dll. Use Create.cpp to create the file Create.dll. Use Remove.cpp to create Remove.dll. Add these dynamic-link library files to the Binary table.

[Binary Table](binary-table.md)



| Name        | Data            |
|-------------|-----------------|
| Process.dll | {*binary data*} |
| Create.dll  | {*binary data*} |
| Remove.dll  | {*binary data*} |



 

Continue to [Adding a Custom CustomUserAccounts Table](adding-a-custom-customuseraccounts-table.md).

 

 



