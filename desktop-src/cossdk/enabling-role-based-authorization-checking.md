---
description: To use role-based security in your COM+ application, you must first enable role-based authorization checking for the application.
ms.assetid: d391a0d4-fe5d-4587-b0b1-b3aa294b7ad7
title: Enabling Role-Based Authorization Checking
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Role-Based Authorization Checking

To use role-based security in your COM+ application, you must first enable role-based authorization checking for the application. This ensures that users who are accessing the application are checked for the role they belong to before they are authorized to do anything in the application. If role-based authorization checking is not enabled, role-based security for the application is not used.

**To enable role-based authorization checking**

1.  Right-click the COM+ application for which you are enabling role-based authorization checking, and then click **Properties**.

2.  In the application properties dialog box, click the **Security** tab.

3.  Under **Authorization**, select the **Enforce access checks for this application** check box; clearing the check box means that role-based security is not used for the application.

4.  Click **OK**.

The selected authorization setting takes effect the next time the application is started.

 

 



