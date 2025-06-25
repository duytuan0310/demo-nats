import nkeys

def generate_nats_credentials() -> dict:
    """
    Generate NATS credentials including seed and public key.
    Returns:
        dict: A dictionary containing the seed and public key.
    """
    keypair = nkeys.KeyPair
    return {
        "seed": keypair.seed,
        "private_key": keypair.private_key,
        "public_key": keypair.public_key
    }

if __name__ == "__main__":
    # Example usage
    credentials = generate_nats_credentials()
    print("NATS Credentials:")
    print(f"Seed: {credentials['seed']}")
    print(f"Private Key: {credentials['private_key']}")
    print(f"Public Key: {credentials['public_key']}")