---
description: You can monitor object statistics as an application runs. By doing so, you can fine-tune the object pool characteristics to achieve the balance in performance and resources that you would like to have.
ms.assetid: 57987cc1-8bb5-4bbd-a425-fda2e5a8b597
title: Monitoring Object Statistics
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring Object Statistics

You can monitor object statistics as an application runs. By doing so, you can fine-tune the object pool characteristics to achieve the balance in performance and resources that you would like to have.

You can monitor status for any objects that are configured to support object statistics and event reporting. Enabling object statistics has a very slight performance overhead.

**To enable object statistics**

1.  In the details pane of the Component Services administrative tool, right-click the component that you want to configure and then click **Properties**.

2.  In the component properties dialog box, click the **Activation** tab.

3.  To enable object statistics for the component, under **Activation Context**, select the **Component supports events and statistics** check box.

**To monitor object status**

1.  In the console tree of the Component Services administrative tool, open the folder for the application that includes the components you want to monitor.

2.  Right-click the **Components** folder, point to **View**, and then click **Status View**. The details pane now displays the status view for all components in the application. The following table describes the six columns in the status view.

    

    | Column                        | Description                                                                                                                                                                                                                |
    |-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **ProgID**<br/>         | Identifies a specific component.<br/>                                                                                                                                                                                |
    | **Objects**<br/>        | Shows the number of objects that are currently held by client references.<br/>                                                                                                                                       |
    | **Activated**<br/>      | Shows the number of objects that are currently activated. <br/>                                                                                                                                                      |
    | **Pooled**<br/>         | Shows the total number of objects created by the pool, including objects that are in use and objects that are deactivated.<br/>                                                                                      |
    | **In Call**<br/>        | Identifies objects in call.<br/>                                                                                                                                                                                     |
    | **Call Time (ms)**<br/> | Shows the average call duration (in milliseconds) of method calls made in the last 20 seconds (up to 20 calls). Call time is measured at the object and does not include the time used to traverse the network.<br/> |

    

     

## Related topics

<dl> <dt>

[Configuring a Component to Be Pooled](configuring-a-component-to-be-pooled.md)
</dt> </dl>

 

 




