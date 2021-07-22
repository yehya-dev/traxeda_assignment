class Router:
    """
    A router to control all database operations on models in the
    traxeda application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to select the database to read from depending on the app name metadata of the model.
        """
        if model._meta.app_label == 'products':
            return 'db_products'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to select the database to write to depending on the app name metadata of the model.
        """
        if model._meta.app_label == 'products':
            return 'db_products'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations ? No Opinion
        """
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Allow migrations ? Yes
        """
        return True
        
