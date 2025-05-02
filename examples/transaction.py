from golem_py.transaction import *


def create_account(username: str, email: str) -> Result[int, str]:
    raise NotImplementedError("TODO: Create the account")


def delete_account(account_id: int) -> Result[None, str]:
    raise NotImplementedError("TODO: Delete the account")


create_account_op: Operation[tuple[str, str], int, str] = operation(
    lambda args: create_account(args[0], args[1]),
    lambda _, account_id: delete_account(account_id),
)


def create_accounts(tx: InfallibleTransaction) -> None:
    tx.execute(create_account_op, ("foo", "foo@golem.com"))
    tx.execute(create_account_op, ("bar", "bar@golem.com"))


infallible_transaction(create_accounts)
