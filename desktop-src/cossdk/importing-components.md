---
description: You can use the Component Services administrative tool to import into applications specific components that have already been registered on your computer as COM components in the Windows registry.
ms.assetid: 5310e08a-5146-41f8-ae65-8467b921abd4
title: Importing Components
ms.topic: article
ms.date: 05/31/2018
---

# Importing Components

You can use the Component Services administrative tool to import into applications specific components that have already been registered on your computer as COM components in the Windows registry. Importing a component does not install the interface or method information required to set interface properties or to configure access to the component from a remote client. Therefore, if possible, you should install rather than import unconfigured components.

> [!Note]  
> When importing a component into a COM+ application, COM+ does not populate interface and method information for the component. During the export of an application proxy, COM+ will not provide marshaling information (type libraries or proxy/stubs) for some or all of the interfaces. Exporting application proxies that contain imported components will fail or cause a warning to be issued.

 

**To import a component into a COM+ application**

1.  In the console tree of the Component Services administrative tool, select the computer hosting the COM+ application.

2.  Open the **COM+ Applications** folder for that computer, and select the application in which you want to install the component.

3.  Open the application folder and select **Components**.

4.  On the **Action** menu, point to **New**, and then click **Component**. You can also right-click the **Components** folder, point to **New**, and then click **Component**.

5.  On the **Welcome** page of the COM+ Application Install Wizard, click **Next**, and then in the **Import or Install a Component** dialog box, click **Import component(s) that are already registered**.

6.  In the **Choose Components to Import** dialog box, select the **Details** check box to see complete information about the components that are already registered. Select the component(s) you want to import from the displayed list, and click **Next**.

7.  Click **Finish**.

## Related topics

<dl> <dt>

[Copying Components](copying-components.md)
</dt> <dt>

[Creating a New COM+ Application](creating-a-new-com--application.md)
</dt> <dt>

[Deleting a COM+ Application](deleting-a-com--application.md)
</dt> <dt>

[Installing New Components](installing-new-components.md)
</dt> <dt>

[Moving Components](moving-components.md)
</dt> <dt>

[Removing a Component from a COM+ Application](removing-a-component-from-a-com--application.md)
</dt> </dl>

 

 



