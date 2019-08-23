---
title: Modifying Existing User Interfaces
description: The results pane of the Active Directory Users and Computers MMC snap-in displays several columns of attribute data for objects within a container, such as the Name and Description attributes.
ms.assetid: 55f4ae82-c380-42a9-beba-047ffd0131eb
ms.tgt_platform: multiple
keywords:
- Modifying Existing User Interfaces AD
- Users and Computers snap-in AD ,modifying display
- Users and Computers snap-in AD ,adding columns
ms.topic: article
ms.date: 05/31/2018
---

# Modifying Existing User Interfaces

The results pane of the Active Directory Users and Computers MMC snap-in displays several columns of attribute data for objects within a container, such as the **Name** and **Description** attributes. The snap-in enables the user to add and remove the columns displayed in the results pane of the snap-in.

To change the display, the user uses the **View** pull-down menu and selects **Add/Remove Columns**. In the **Add/Remove Columns** dialog box, there is a list of columns that the user can choose from to display in the results pane.

The Active Directory Users and Computers MMC snap-in that is included with Windows Server 2003, Standard Edition, Windows Server 2003, Enterprise Edition, and Windows Server 2003, Datacenter Edition, provides the ability to modify the list of columns that can be displayed in the results pane of the snap-in for a container. This feature only exists if the snap-in is targeted at a forest with Windows Server 2003 schema.

To add a column to the list, add a value to the **extraColumns** attribute of the display specifier for the object type that the attribute is associated with. The **extraColumns** attribute is a multi-valued string attribute where each string is in the following format.


```C++

<ldapdisplayname>,<column header>,<default visibility>,<width>,<unused>

```



The following table lists the contents of these values.



| Value                        | Description                                                                                                                         |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| "&lt;ldapdisplayname&gt;"    | Contains a string that represents the **ldapDisplayName** of the attribute.                                                         |
| "&lt;column header&gt;"      | Contains a string that represents the text displayed in the header for the column.                                                  |
| "&lt;default visibility&gt;" | Contains a numeric value that is 0 if the attribute is hidden by default or 1 if the attribute is visible by default.               |
| "&lt;width&gt;"              | Contains the width of the column, in pixels. If this value is -1, the width of the column is set to the width of the column header. |
| "&lt;unused&gt;"             | Unused. Must be zero.                                                                                                               |



 

For example, to add a column that will display the canonical name for objects in an organizational unit, a value for the **canonicalName** attribute is added to the **extraColumns** attribute of the **organizationalUnit-Display** object in the display specifiers container. The string added to the **extraColumns** attribute of the **organizationalUnit-Display** object will look like the following.


```C++
canonicalName,Canonical Name,0,150,0
```



The **Add/Remove Columns** dialog box displays only the columns that are contained in the **extraColumns** attribute of the **displaySpecifier** object of the container type that is being displayed. If the **extraColumns** attribute does not contain any values, the **Add/Remove Columns** dialog box will display a fixed set of columns. A copy of the fixed set of columns is contained in the **extraColumns** attribute of the **default-Display** object.

To add one or more columns to the list of columns for a specific object, you must copy all of the **extraColumns** values from the **default-Display** object to the target object and then add the custom columns. If you specify the **extraColumns** attribute on a given class, then that class will use those columns and will not merge them with the columns that are specified in the **default-Display** class. Therefore, further changes to the **default-Display** class will have no effect on that object.

To display a custom column for all container types that do not have any custom columns registered, add a value for the column to the **extraColumns** attribute of the **default-Display** object.

 

 




