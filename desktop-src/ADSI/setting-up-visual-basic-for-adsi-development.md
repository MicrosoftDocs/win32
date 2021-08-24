---
title: Setting Up Visual Basic 6.0 for ADSI Development
description: This topic discusses how to set up Visual Basic in Visual Studio to develop an ADSI application.
ms.assetid: 167e89d7-80a3-4cc2-b79c-3744c1b184d6
ms.tgt_platform: multiple
keywords:
- Setting Up Visual Basic for ADSI Development ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Setting Up Visual Basic 6.0 for ADSI Development

**Setting Up the Microsoft Visual Studio 2010 Development Environment For Visual Basic**

1.  Start Visual Studio 2010.
2.  Create a new Visual Basic project.
3.  Add a reference to the **Active DS Type Library**.
    > [!Note]  
    > If you do not require early COM object binding, ignore this step.

     

    1.  Select **Project \| Add Reference**.
    2.  Select the **COM** tab.
    3.  Select **Active DS Type Library**.

4.  Begin programming with ADSI.

Before you begin, log on to a Windows domain. You must have permission to modify the Active Directory database. By default, the Administrator has this privilege.

**A Sample Visual Basic 6.0 Application: Modifying FullName and Description for a User**

1.  Follow the previous steps to create a standard executable Visual Basic project.
2.  Double-click the Form. In Form\_Load, type the following. You must replace the "LDAP://CN=jeffsmith,CN=users,DC=fabrikam,DC=com" string with the ADsPath of an existing user in a container in your domain. Create a test user account that can be modified for this purpose.
    ```VB
    '------------------------------------------------------------
    ' This code example is used to set the FullName and Description
    '------------------------------------------------------------
    Dim usr As IADsUser

    ' Bind to a user object.
    Set usr = GetObject("LDAP://CN=jeffsmith,CN=users,DC=fabrikam,DC=com")

    usr.FullName = "Jeff Smith"
    usr.Description = "A user for fabrikam.com" 
    usr.SetInfo ' Commit the changes to the directory
    ```

    

3.  Press **&lt;F5&gt;** to run the program.
4.  To verify changes, use the Active Directory Users and Computers management tool. For more information about using ADSI and Visual Basic, see [Accessing Active Directory Using Visual Basic](accessing-active-directory-using-visual-basic.md).

 

 




