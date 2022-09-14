---
description: As existing applications become dated or are no longer being used, you may need to remove them.
ms.assetid: 5cce94c9-8eff-40b9-946d-a57749da073d
title: Deleting a COM+ Application
ms.topic: article
ms.date: 05/31/2018
---

# Deleting a COM+ Application

As existing applications become dated or are no longer being used, you may need to remove them.

**To delete a COM+ application**

1.  In the console tree of the Component Services administrative tool, select the computer for which you want to delete an application.

2.  Open the **COM+ Applications** folder for the specified computer to display all the applications.

3.  Select the application you want to remove.

4.  If you selected a server application, shut down the application. You can shut down an application by selecting it in the Component Services administrative tool, right-clicking, and then clicking **Shut down**. If you selected a library application, make sure that all processes currently using this library application are shut down.

5.  On the **Action** menu, click **Delete**. You can also right-click the application name and then click **Delete**. You can also delete an application by selecting it in the Component Services administrative tool and pressing the **Delete** key, or you can select the application, right-click, and then click **Delete**.

6.  Click **Yes** when prompted to confirm your action.

In addition, if a server application or application proxy has been installed on a computer using Windows Installer (as described in "Installing COM+ Applications" in the Component Services Administration Guide), you can delete it through the Add/Remove Programs utility in the Microsoft Windows Control Panel. Or you can delete an installed server application or application proxy by using the Windows Installer command line syntax:

**msiexec -x** *application\_name***.msi**

These methods are especially useful for deleting COM+ applications on client machines that are not running the Component Services administrative tool.

Deleting the application also deletes any components contained in the application. If these components depend on additional resources (database connections, data or text files, IIS virtual root configuration, and so on), these resources must be removed through mechanisms other than the Component Services administrative tool.

## Related topics

<dl> <dt>

[Copying Components](copying-components.md)
</dt> <dt>

[Creating a New COM+ Application](creating-a-new-com--application.md)
</dt> <dt>

[Importing Components](importing-components.md)
</dt> <dt>

[Installing New Components](installing-new-components.md)
</dt> <dt>

[Moving Components](moving-components.md)
</dt> <dt>

[Removing a Component from a COM+ Application](removing-a-component-from-a-com--application.md)
</dt> </dl>

 

 



