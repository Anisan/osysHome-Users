# User guide — Users

The **Users** module manages accounts in `osysHome`: who can sign in, which permissions they receive, and which profile settings are assigned to them.

> [!IMPORTANT]
> User creation, password changes, and assigning the **Administrator** role should be limited to trusted administrators.

## Module purpose

With `Users`, an administrator can manage accounts by:

- creating new users;
- assigning roles;
- configuring the start page after sign-in;
- selecting a timezone;
- setting or rotating an `API key`;
- uploading an avatar;
- setting a password;
- deleting accounts that are no longer needed.

In practice, the module acts as an administrative editor for `Users` class objects.

## Where to find it

Open the top **Administration** menu and select **Users**.

## What is shown on the main page

The main table usually displays:

- avatar and username;
- role;
- home page;
- last login time;
- **Edit**, **Set password**, and **Delete** buttons.

The **Add user** button opens the new-account form.

## Core operations

### Create a user

1. Click **Add user**.
2. Enter **Username**.
3. Choose **Role**.
4. Fill in **Home page**, **Timezone**, and **API key** if needed.
5. Click **Submit**.
6. After the user is created, open the record and run **Set password**.

> [!TIP]
> If an `API key` is needed for integrations, you can generate it later from the user form instead of typing it manually.

### Edit a user profile

1. Click **Edit** on the required row.
2. Update the profile fields.
3. Click **Submit** to save changes.

Typical edits include:

- role;
- home page;
- timezone;
- `API key`;
- avatar.

> [!NOTE]
> Treat the username as a stable account identifier. If a real rename is required, it is safer to create a new account and move access manually.

### Upload or replace an avatar

1. Open the user through **Edit**.
2. Click the upload button on the avatar card.
3. Select an image file.
4. Confirm the upload.

After a successful upload, the new avatar is shown immediately in the user card and in the user list.

### Generate a new API key

1. Open the user form through **Edit**.
2. Locate the **API key** field.
3. Click **Generate key**.
4. Save the changes with **Submit**.

This is useful when a key must be issued to an external script or rotated after a suspected leak.

### Set or change a password

1. Click **Set password** for the selected user.
2. Fill in **New password** and **Repeat password** with the same value.
3. Click **Submit**.

If the values do not match, the password will not be saved.

> [!NOTE]
> A password is not entered directly during user creation. After the account is created, you set it in a separate step.

### Delete a user

1. Click **Delete** in the row of the required user.
2. Confirm the deletion.

> [!WARNING]
> Account deletion is permanent. If you only need to reduce access temporarily, it is safer to lower the user role first.

## Access roles

| Role | Purpose |
| --- | --- |
| **Guest** | Minimal access, usually limited to viewing the interface and data. |
| **User** | Basic day-to-day access for regular work in the system. |
| **Editor** | Permission to modify data where editing is allowed. |
| **Administrator** | Full administrative access, including user management. |

> [!IMPORTANT]
> The **Administrator** role provides full control over the system. Assign it only to people who truly need administrative access.

## Profile fields

### Username

The unique account name used for sign-in and user identification in the system.

### Role

Defines which level of access the user has to system sections and administrative actions.

### Home page

The page opened immediately after sign-in. Typical values look like `/` or `/admin`.

### Timezone

The user's timezone. It affects how event times, logs, and last-login values are displayed in the interface.

### API key

A secret key for external integrations, scripted requests, and other automation scenarios.

Recommended practices:

- do not share it in open messages;
- rotate it if you suspect a leak;
- keep it only in integrations that actually require it.

### Avatar

The profile image shown in the edit card and the users list.

## Typical scenarios

### Grant access to a new employee

1. Create a user through **Add user**.
2. Assign the minimum required role.
3. Set the home page and timezone.
4. Generate an `API key` if integrations require one.
5. Set the password through **Set password**.
6. Deliver the login and temporary credentials securely.

### Reset a password

1. Find the required user in the list.
2. Open **Set password**.
3. Enter the new password twice.
4. Save the change and share the new credentials securely.

### Reduce permissions

1. Open the user through **Edit**.
2. Lower the role to the appropriate level.
3. Save the change.
4. Check whether any old integrations still use an active `API key`.

### Revoke access completely

1. Confirm that the account is no longer needed.
2. Preserve related data first if audit history matters.
3. Remove the user through **Delete**.

## Administrator checklist

- [ ] Every user has a strong password.
- [ ] The **Administrator** role is granted only where truly necessary.
- [ ] User timezones are configured correctly.
- [ ] Unused or compromised `API key` values have been rotated.
- [ ] User deletion is performed only after checking the consequences.

## Recommended access-grant flow

1. Create the user.
2. Assign the role.
3. Verify profile data and timezone.
4. Generate an `API key` if needed.
5. Set the password.
6. Confirm that the correct start page opens for the user.
