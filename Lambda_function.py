// Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

import { SESClient, SendEmailCommand } from "@aws-sdk/client-ses";
const ses = new SESClient({ region: "us-east-1" });

export const handler = async (event) => {
  const command = new SendEmailCommand({
    Destination: {
      ToAddresses: ["pra56.kum61@gmail.com"],
    },
    Message: {
      Body: {
        Text: { Data: "Test" },
      },

      Subject: { Data: "Test Email" },
    },
    Source: "no-reply-aws@amazon.com",
  });

  try {
    let response = await ses.send(command);
    // process data.
    return response;
  } catch (error) {
    // error handling.
  } finally {
    // finally.
  }
};