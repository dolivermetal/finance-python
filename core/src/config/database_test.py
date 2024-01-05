from core.src.config.database import DatabaseManager


def test_create_engine():
    db_manager = DatabaseManager()
    engine = db_manager.get_engine()

    assert engine is not None