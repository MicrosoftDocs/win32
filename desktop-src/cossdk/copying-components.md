---
description: You can copy a component from one COM+ application to another. After you copy a component to another COM+ application, you can configure this component differently than the original component.
ms.assetid: 49dfd449-05eb-4442-989f-15bc1586d8c5
title: Copying Components
ms.topic: article
ms.date: 05/31/2018
---

# Copying Components

You can copy a component from one COM+ application to another. After you copy a component to another COM+ application, you can configure this component differently than the original component.

**To copy a component from one COM+ application to another**

1.  In the details pane of the Component Services administrative tool, right-click the component that you want to copy and then click **Copy**.

2.  In the **Copy Component** dialog box, in the **Please select a Destination** pane, select the COM+ application to which the component will be copied.

3.  Enter the new ProgID for the copied component.

    > [!Note]  
    > The ProgID for the original component is displayed for reference and cannot be changed.

     

4.  Enter the new CLSID for the copied component. COM+ displays an automatically generated CLSID. In most cases, this will be sufficient to uniquely identify the copied component. Enter a new CLSID only if you want to change the one provided by COM+.

5.  Click **OK**.

## Related topics

<dl> <dt>

[Creating a New COM+ Application](creating-a-new-com--application.md)
</dt> <dt>

[Deleting a COM+ Application](deleting-a-com--application.md)
</dt> <dt>

[Importing Components](importing-components.md)
</dt> <dt>

[Installing New Components](installing-new-components.md)
</dt> <dt>

[Moving Components](moving-components.md)
</dt> <dt>

[Removing a Component from a COM+ Application](removing-a-component-from-a-com--application.md)
</dt> </dl>

 

 



