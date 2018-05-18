---
title: Android code examples
description: This topic will introduce you to important code elements for the Android version of the RMS SDK.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '58CC2E50-1E4D-4621-A947-25312C3FF519'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# Android code examples

This topic will introduce you to important code elements for the Android version of the RMS SDK.

> [!Note]  
> In the example code and descriptions that follow, we use the term MSIPC (Microsoft Information Protection and Control) to reference the client process.

 

## Using the Rights Management SDK 4.2 - key scenarios

Following are code examples from a larger sample application representing development scenarios important to your orientation to this SDK. These demonstrate; use of Microsoft Protected File format referred to as protected file , use of custom protected file formats, and use of custom UI controls.

The sample application, *MSIPCSampleApp*, is available for use with this SDK for the Android operating system. See [rms-sdk-ui-for-android](https://github.com/AzureAD/rms-sdk-ui-for-android) on GitHub for access to this sample application.

## **Scenario**: Consume an RMS protected file

-   **Step 1**: Create a [**ProtectedFileInputStream**](protectedfileinputstream-class-java.md)

    **Source**: *MsipcAuthenticationCallback.java*

    **Description**: Instantiate a [**ProtectedFileInputStream**](protectedfileinputstream-class-java.md) object, through its create method which implements service authentication using the [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md) to get a token by passing an instance of **AuthenticationRequestCallback**, as the parameter *mRmsAuthCallback*, to the MSIPC API. See the call to [**ProtectedFileInputStream.create**](protectedfileinputstream-create-method.md) near the end of the following example code section.

    ```Java
    public void startContentConsumptionFromPtxtFileFormat(InputStream inputStream)
        {
            CreationCallback<ProtectedFileInputStream> protectedFileInputStreamCreationCallback = 
              new CreationCallback<ProtectedFileInputStream>()
            {
                @Override
                public Context getContext()
                {
                   …
               }

                @Override
                public void onCancel()
                {
                   …
                }

                @Override
                public void onFailure(ProtectionException e)
                {
                   …
                }

                @Override
                public void onSuccess(ProtectedFileInputStream protectedFileInputStream)
                {
                   …
                   …
                    byte[] dataChunk = new byte[16384];
                    try
                    {
                        while ((nRead = protectedFileInputStream.read(dataChunk, 0, 
                                dataChunk.length)) != -1)
                        {
                            …
                        }
                         …
                        protectedFileInputStream.close();
                    }
                    catch (IOException e)
                    {
                      …
                    }  
              }
            };
            try
            {
               …
                ProtectedFileInputStream.create(inputStream, null, mRmsAuthCallback, 
                                                PolicyAcquisitionFlags.NONE, 
                                                protectedFileInputStreamCreationCallback);
            }
            catch (com.microsoft.rightsmanagement.exceptions.InvalidParameterException e)
            {
                …
            }
        }
    ```

    

-   **Step 2**: Setup authentication using the Active Directory Authentication Library (ADAL).

    **Source**: *MsipcAuthenticationCallback.java*.

    <dl> **Description**: In this step you will see ADAL used to implement an [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md) with example authentication parameters. For more information on using ADAL, see the [Azure AD Authentication Library (ADAL)](https://msdn.microsoft.com/library/jj573266.aspx).

    ```Java
    class MsipcAuthenticationCallback implements AuthenticationRequestCallback
    {

        ...
        ...

        @Override
        public void getToken(Map<String, String> authenticationParametersMap,
                             final AuthenticationCompletionCallback authenticationCompletionCallbackToMsipc)
        {
            String authority = authenticationParametersMap.get("oauth2.authority");
            String resource = authenticationParametersMap.get("oauth2.resource");
            String userId = authenticationParametersMap.get("userId");
            final String userHint = (userId == null)? "" : userId; 
            AuthenticationContext authenticationContext = App.getInstance().getAuthenticationContext();
            if (authenticationContext == null || !authenticationContext.getAuthority().equalsIgnoreCase(authority))
            {
                try
                {
                    authenticationContext = new AuthenticationContext(App.getInstance().getApplicationContext(), authority, …);
                    App.getInstance().setAuthenticationContext(authenticationContext);
                }
                catch (NoSuchAlgorithmException e)
                {
                    …
                    authenticationCompletionCallbackToMsipc.onFailure();
                }
                catch (NoSuchPaddingException e)
                {
                    …
                    authenticationCompletionCallbackToMsipc.onFailure();
                }
           }
            App.getInstance().getAuthenticationContext().acquireToken(mParentActivity, resource, mClientId, mRedirectURI, userId, mPromptBehavior,
                           "&amp;USERNAME=" + userHint, new AuthenticationCallback<AuthenticationResult>()
                            {
                                @Override
                                public void onError(Exception exc)
                                {
                                    …
                                    if (exc instanceof AuthenticationCancelError)
                                    {
                                         …
                                        authenticationCompletionCallbackToMsipc.onCancel();
                                    }
                                    else
                                    {
                                         …
                                        authenticationCompletionCallbackToMsipc.onFailure();
                                    }
                                }

                                @Override
                                public void onSuccess(AuthenticationResult result)
                                {
                                    …
                                    if (result == null || result.getAccessToken() == null
                                            || result.getAccessToken().isEmpty())
                                    {
                                         …
                                    }
                                    else
                                    {
                                        // request is successful
                                        …
                                        authenticationCompletionCallbackToMsipc.onSuccess(result.getAccessToken());
                                    }
                                }
                            });
                             }
    
    ```

    

      
    </dl>

-   **Step 3**: Check if the **Edit** right exists for this user with this content via the [**accessCheck**](userpolicy-accesscheck-method-java.md) method of [**UserPolicy**](userpolicy-class-java.md).

    **Source**: *TextEditorFragment.java*

    ```Java
             //check if user has edit rights and apply enforcements
                if (!mUserPolicy.accessCheck(EditableDocumentRights.Edit))
                {
                    mTextEditor.setFocusableInTouchMode(false);
                    mTextEditor.setFocusable(false);
                    mTextEditor.setEnabled(false);
                    …
                }
    ```

    

## **Scenario**: Create a new protected file using a template

This scenario begins with getting a list of templates, selecting the first one to create a policy, then creates and writes to the new protected file.

-   <dl> **Step 1**: Get list of templates via a [**TemplateDescriptor**](templatedescriptor-class-java.md) object.**Source**: *MsipcTaskFragment.java*  
    **Description**: TBD  
    ```Java
    CreationCallback<List<TemplateDescriptor>> getTemplatesCreationCallback = new CreationCallback<List<TemplateDescriptor>>()
      {
          @Override
          public Context getContext()
          {
              …
          }

          @Override
          public void onCancel()
          {
              …
          }

          @Override
          public void onFailure(ProtectionException e)
          {
              …
          }

          @Override
          public void onSuccess(List<TemplateDescriptor> templateDescriptors)
          {
             …
          }
      };
      try
      {
              …
          mIAsyncControl = TemplateDescriptor.getTemplates(emailId, mRmsAuthCallback, getTemplatesCreationCallback);
      }
      catch (com.microsoft.rightsmanagement.exceptions.InvalidParameterException e)
      {
              …
      }
    ```

    

    **Step 2**: Create a [**UserPolicy**](userpolicy-class-java.md) using the first template in the list.**Source**: *MsipcTaskFragment.java*  
    **Description**: TBD  
    ```Java
     CreationCallback<UserPolicy> userPolicyCreationCallback = new CreationCallback<UserPolicy>()
     {
          @Override
          public Context getContext()
          {
              …
          }

          @Override
          public void onCancel()
          {
              …
          }

          @Override
          public void onFailure(ProtectionException e)
          {
              …
          }

          @Override
          public void onSuccess(final UserPolicy item)
          {
              …
          }
      };
      try
      {
           …
          mIAsyncControl = UserPolicy.create((TemplateDescriptor)selectedDescriptor, mEmailId, mRmsAuthCallback,
                            UserPolicyCreationFlags.NONE, userPolicyCreationCallback);
           …
      }
      catch (InvalidParameterException e)
      {
              …
      }
    ```

    

    **Step 3**: Create a [**ProtectedFileOutputStream**](protectedfileoutputstream-class-java.md) and write content to it.**Source**: *MsipcTaskFragment.java*  
    **Description**: TBD  
    ```Java
       private void createPTxt(final byte[] contentToProtect)
        {
             …
            CreationCallback<ProtectedFileOutputStream> protectedFileOutputStreamCreationCallback = new CreationCallback<ProtectedFileOutputStream>()
            {
                @Override
                public Context getContext()
                {
                 …
                }

                @Override
                public void onCancel()
                {
                 …
                }

                @Override
                public void onFailure(ProtectionException e)
                {
                 …
                }

                @Override
                public void onSuccess(ProtectedFileOutputStream protectedFileOutputStream)
                {
                    try
                    {
                        // write to this stream
                        protectedFileOutputStream.write(contentToProtect);
                        protectedFileOutputStream.flush();
                        protectedFileOutputStream.close();
                        …
                    }
                    catch (IOException e)
                    {
                        …
                    }
                }
            };
            try
            {
                File file = new File(filePath);
                outputStream = new FileOutputStream(file);
                mIAsyncControl = ProtectedFileOutputStream.create(outputStream, mUserPolicy, originalFileExtension,
                        protectedFileOutputStreamCreationCallback);
            }
            catch (FileNotFoundException e)
            {
                 …
            }
            catch (InvalidParameterException e)
            {
                 …
            }
        }
    ```

    

    </dl>

## **Scenario**: Open a custom protected file

-   <dl> **Step 1**: Create a [**UserPolicy**](userpolicy-class-java.md) from a *serializedContentPolicy*.**Source**: *MsipcTaskFragment.java*
    ```Java
    CreationCallback<UserPolicy> userPolicyCreationCallbackFromSerializedContentPolicy = new CreationCallback<UserPolicy>()
            {
                @Override
                public void onSuccess(UserPolicy userPolicy)
                {
                  …
                }

                @Override
                public void onFailure(ProtectionException e)
                {
                  …
                }

                @Override
                public void onCancel()
                {
                  …
                }

                @Override
                public Context getContext()
                {
                  …
                }
            };


    try
    {
      ...

      // Read the serializedContentPolicyLength from the inputStream.
      long serializedContentPolicyLength = readUnsignedInt(inputStream);

      // Read the PL bytes from the input stream using the PL size.
      byte[] serializedContentPolicy = new byte[(int)serializedContentPolicyLength];
      inputStream.read(serializedContentPolicy);

      ...
                
      UserPolicy.acquire(serializedContentPolicy, null, mRmsAuthCallback, PolicyAcquisitionFlags.NONE,
              userPolicyCreationCallbackFromSerializedContentPolicy);
    }
    catch (com.microsoft.rightsmanagement.exceptions.InvalidParameterException e)
    {
      ...
    }
    catch (IOException e)
    {
      ...
    }
      
    ```

    

      
    **Step 2**: Create a [**CustomProtectedInputStream**](customprotectedinputstream-class-java.md) using the [**UserPolicy**](userpolicy-class-java.md) from **Step 1**.**Source**: *MsipcTaskFragment.java*
    ```Java
     CreationCallback<CustomProtectedInputStream> customProtectedInputStreamCreationCallback = new CreationCallback<CustomProtectedInputStream>()
     {
         @Override
         public Context getContext()
         {
             …
         }

         @Override
         public void onCancel()
         {
             …
         }

         @Override
         public void onFailure(ProtectionException e)
         {
             …
         }

         @Override
         public void onSuccess(CustomProtectedInputStream customProtectedInputStream)
         {
            …

             byte[] dataChunk = new byte[16384];
             try
             {
                 while ((nRead = customProtectedInputStream.read(dataChunk, 0, dataChunk.length)) != -1)
                 {
                      …
                 }
                  …
                 customProtectedInputStream.close();
             }
             catch (IOException e)
             {
                …
             }
             …
         }
     };

    try
    {
      ...
                        
      // Retrieve the encrypted content size.
      long encryptedContentLength = readUnsignedInt(inputStream);
                        
      updateTaskStatus(new TaskStatus(TaskState.Starting, "Consuming content", true));
                        
      CustomProtectedInputStream.create(userPolicy, inputStream, 
                                     encryptedContentLength,
                                     customProtectedInputStreamCreationCallback);
    }
    catch (com.microsoft.rightsmanagement.exceptions.InvalidParameterException e)
    {
      ...
    }
    catch (IOException e)
    {
      ...
    }
    ```

    

      
    **Step 3**: Read content from the [**CustomProtectedInputStream**](customprotectedinputstream-class-java.md) into *mDecryptedContent* then close.**Source**: *MsipcTaskFragment.java*
    ```Java
    @Override
    public void onSuccess(CustomProtectedInputStream customProtectedInputStream)
    {
      mUserPolicy = customProtectedInputStream.getUserPolicy();
      ByteArrayOutputStream buffer = new ByteArrayOutputStream();
                            
      int nRead;                      
      byte[] dataChunk = new byte[16384];

      try
      {
        while ((nRead = customProtectedInputStream.read(dataChunk, 0, 
                                                            dataChunk.length)) != -1)
        {
           buffer.write(dataChunk, 0, nRead);
        }
                                
        buffer.flush();
        mDecryptedContent = new String(buffer.toByteArray(), Charset.forName("UTF-8"));
        
        buffer.close();
        customProtectedInputStream.close();
      }
      catch (IOException e)
      {
        ...
      }
    }
    ```

    

      
    </dl>

## **Scenario**: Create a custom protected file using a custom (ad-hoc) policy

-   <dl> **Step 1**: With an email address provided by the user, create a policy descriptor. **Source**: *MsipcTaskFragment.java*  
    **Description**: In practice the following objects would be created by using user inputs from the device interface; [**UserRights**](userrights-class-java.md) and [**PolicyDescriptor**](policydescriptor-interface-java.md).  
    ```Java
    
      ...

      // create userRights list
      UserRights userRights = new UserRights(Arrays.asList("consumer@domain.com"), 
        Arrays.asList( CommonRights.View, EditableDocumentRights.Print));
      ArrayList<UserRights> usersRigthsList = new ArrayList<UserRights>();
      usersRigthsList.add(userRights);
           
      // Create PolicyDescriptor using userRights list
      PolicyDescriptor policyDescriptor = PolicyDescriptor.createPolicyDescriptorFromUserRights(
                                                             usersRigthsList);
      policyDescriptor.setOfflineCacheLifetimeInDays(10);
      policyDescriptor.setContentValidUntil(new Date());
      
      ...
    ```

    

    **Step 2**: Create a custom [**UserPolicy**](userpolicy-class-java.md) from the policy descriptor, *selectedDescriptor*. **Source**: *MsipcTaskFragment.java*
    ```Java
      
       ...
       mIAsyncControl = UserPolicy.create((PolicyDescriptor)selectedDescriptor, 
                                              mEmailId, mRmsAuthCallback,
                                              UserPolicyCreationFlags.NONE, 
                                              userPolicyCreationCallback);
       ...
    
    ```

    

      
    </dl>
-   **Step 3**: Create and write content to the [**CustomProtectedOutputStream**](customprotectedoutputstream-class-java.md) and then close.

    **Source**: *MsipcTaskFragment.java*

    ```Java
        File file = new File(filePath);
        final OutputStream outputStream = new FileOutputStream(file);
        CreationCallback<CustomProtectedOutputStream> customProtectedOutputStreamCreationCallback = new CreationCallback<CustomProtectedOutputStream>()
        {
            @Override
            public Context getContext()
            {
              …
            }

            @Override
            public void onCancel()
            {
              …
            }

            @Override
            public void onFailure(ProtectionException e)
            {
              …
            }

            @Override
            public void onSuccess(CustomProtectedOutputStream protectedOutputStream)
            {
                try
                {
                    // write serializedContentPolicy
                    byte[] serializedContentPolicy = mUserPolicy.getSerializedContentPolicy();
                    writeLongAsUnsignedIntToStream(outputStream, serializedContentPolicy.length);
                    outputStream.write(serializedContentPolicy);
                    // write encrypted content
                    if (contentToProtect != null)
                    {
                        writeLongAsUnsignedIntToStream(outputStream,
                                CustomProtectedOutputStream.getEncryptedContentLength(contentToProtect.length,
                                        protectedOutputStream.getUserPolicy()));
                        protectedOutputStream.write(contentToProtect);
                        protectedOutputStream.flush();
                        protectedOutputStream.close();
                    }
                    else
                    {
                        outputStream.flush();
                        outputStream.close();
                    }
                    …
                }
                catch (IOException e)
                {
                  …
                }
            }
        };
        try
        {
            mIAsyncControl = CustomProtectedOutputStream.create(outputStream, mUserPolicy,
                    customProtectedOutputStreamCreationCallback);
        }
        catch (InvalidParameterException e)
        {
          …
        }
    ```

    

 

 




