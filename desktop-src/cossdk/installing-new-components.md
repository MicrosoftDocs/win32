---
description: To add components to the Components folder of a COM+ application, you can either use the COM+ Component Install Wizard or drag .dll files that contain the components from the Windows Explorer and drop them in the application.
ms.assetid: 3cb0c24d-cd52-42ac-8b07-d8774698b90c
title: Installing New Components
ms.topic: article
ms.date: 05/31/2018
---

# Installing New Components

To add components to the **Components** folder of a COM+ application, you can either use the COM+ Component Install Wizard or drag .dll files that contain the components from the Windows Explorer and drop them in the application.

If you use the COM+ Component Install Wizard, you can either install a new component, which registers the component on the computer, or import components that have already been registered. Components can be added to empty applications or existing applications.

**To add a component to a COM+ application**

1.  In the console tree of the Component Services administrative tool, select the computer hosting the COM+ application.

2.  Open the **COM+ Applications** folder for that computer, and select the application in which you want to install the component(s).

3.  Open the application folder and select **Components**.

4.  On the **Action** menu, point to **New**, and then click **Component**. You can also right-click the **Components** folder, point to **New**, and then click **Component**.

5.  On the **Welcome** page of the COM+ Application Install Wizard, click **Next**, and then in the **Import or Install a Component** dialog box, click **Install new components** .

6.  In the **Install new components** dialog box, click **Add** to browse for the component you want to add.

7.  In the **Select files to install** dialog box, type the filename of the component to install or select a filename from the displayed list. Click **Open**.

    After you add the files, the **Install new components** dialog box displays the files you have added and their associated components. If you select the **Details** check box, you will see more information about file contents and the components that were found.

    > [!Note]  
    > Unconfigured COM components must have a type library. If COM+ cannot find your component's type library, your component will not appear in the list. You can also remove a file from the **Files to install** list by selecting it and clicking **Remove**.

     

8.  Click **Next**, and then click **Finish** to install the component.

## Related topics

<dl> <dt>

[Copying Components](copying-components.md)
</dt> <dt>

[Creating a New COM+ Application](creating-a-new-com--application.md)
</dt> <dt>

[Deleting a COM+ Application](deleting-a-com--application.md)
</dt> <dt>

[Importing Components](importing-components.md)
</dt> <dt>

[Moving Components](moving-components.md)
</dt> <dt>

[Removing a Component from a COM+ Application](removing-a-component-from-a-com--application.md)
</dt> </dl>

 

 



