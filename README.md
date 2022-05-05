# Idempotent cleanup test

Mini project to test PR: [feat(idempotency): Clean up after lambda timeout](https://github.com/awslabs/aws-lambda-powertools-python/pull/1198)

## Deploying

First time deploy

```bash
sam build
sam deploy --guided
```

Incremental deploy

```bash
sam deploy --guided
```

## Testing

To trigger a clean up invoke the deployed lambda twice. First will create the "INPROGRESS" record with a
`function_timeout` set to current time plus function timeout. Second invoke will delete the "INPROGRESS" record,
and execute the handler again.

Testing happy flow: Update `src/app.py` line 21 to be `time.sleep(0.1)`. Then inoking will succeed and follow up
invokes will return the original response.

Test Cases:

- `IdempotencyOldFunction` - Tests old behavior when a function times out and a inprogress record is created.
- `IdempotencyTimeoutFunction` - Tests new option to clean up inprogress records after timeout.
- `IdempotencyFunction` - Check happy path still works
