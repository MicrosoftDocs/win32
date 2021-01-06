---
description: A COM+ server application can be created as a service to start either automatically during the system startup or manually by activations.
ms.assetid: 56487746-328d-4435-af58-368aaa15b32a
title: Configuring a COM+ Server Application as a Service Application
ms.topic: article
ms.date: 05/31/2018
---

# Configuring a COM+ Server Application as a Service Application

A COM+ server application can be created as a service to start either automatically during the system startup or manually by activations. If the service fails to start, the option for error handling specifies the severity of the error and determines the action to be taken. The option to configure a service to run as the local system account is also available, as well as the option to assign a specific user account for which the COM+ server application will run. Dependencies can also be selected from a list of services registered on the computer using Component Services. This will determine which services must be executed before this service is started.

**To configure a COM+ application to run as a service**

1.  In the console tree of the Component Services administrative tool, locate the COM+ server application you want to run as a service.

2.  Right-click the COM+ server application, and then click **Properties**.

3.  In the **Properties** dialog box, click the **Activation** tab.

4.  In the **Activation type** box, check the **Run application as NT Service** check box.

    > [!Note]  
    > The **Run application as NT Service** check box is enabled only for server applications and is disabled for library applications.

     

5.  Click the **Setup New Service** button.

6.  In the **Startup type** box in the **Service Name** dialog box, select **Automatic** or **Manual**.

7.  (Optional) To specify the action to be taken for a particular error, select **Ignore**, **Normal**, **Severe**, or **Critical** in the **Error Handling** box. The behavior associated with each option is as follows:

    1.  **Ignore**. The startup program logs the error but continues the startup operation.
    2.  **Normal**. The error is logged, a message box is displayed, and the startup program continues the startup operation.
    3.  **Severe**. The error is logged, and the system is restarted with the last known good configuration. If it is the last known good configuration that is being started when the error is logged, the startup operation continues.
    4.  **Critical**. The error is logged, and the system is restarted with the last known good configuration. If it is the last known good configuration that is being started when the error is logged, the startup operation fails.

8.  (Optional) To set other services as dependent, select the dependent services from the list in the **Dependencies** box.

9.  (Optional) To indicate that the service should be allowed to interact with the desktop, check the **Allow service to interact with desktop** check box.

10. Click **Create**.

11. (Optional) To assign the service to a user account:

    1.  In the **Identity** tab, select **This user**.
    2.  To select the user, enter the user name in the **User** box or click the **Browse** button.
    3.  Enter the password for the user account in the **Password** box.
    4.  Enter the same password in the **Confirm Password** box.

 

 



